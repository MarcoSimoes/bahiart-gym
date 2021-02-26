import socket
import threading

class Proxy:

    def __init__(self,server_host, server_port, agent_port):

        self.SERVER_HOST = 'localhost'
        self.SERVER_PORT = server_port
        self.AGENT_PORT = agent_port

        # AGENT CONNECTION INITIAL SETUP
        self.agentSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.agentSock.bind((self.SERVER_HOST, self.AGENT_PORT))

        # SERVER CONNECTION INITIAL SETUP
        self.serverSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connectToServer(self):
        self.serverSock.connect((self.SERVER_HOST, self.SERVER_PORT))
        print("[PROXY]Connected to server on port : " + str(self.SERVER_PORT))

    def connectNewAgents(self):

        print('[PROXY]Waiting agent to connect on port : ' + str(self.AGENT_PORT))
        agentList = []
        count = 0
        while True:
            self.agentSock.listen()
            newAgentSock, _ = self.agentSock.accept()
            agentList.insert(count,newAgentSock)
            print('[PROXY]new agent connected')

            self.connectToServer()

            connectionAgentToServer = threading.Thread(target=self.connectionManager,args=(agentList[count],self.serverSock,'[AGENT - SERVER]'))
            connectionServerToAgent = threading.Thread(target=self.connectionManager,args=(self.serverSock,agentList[count],'[SERVER - AGENT]'))

            connectionAgentToServer.start()
            connectionServerToAgent.start()
            count += 1

    # MUST NOT CALL // PRIVATE
    def sendTo(self,sock,message):
        print("SENT")
        print(message.decode)
        sock.sendall(message)

    # MUST NOT CALL // PRIVATE
    def connectionManager(self,listenSock,sendSock,who):
        # Initializing variable
        message = ''.encode() 
        while True:
            length = listenSock.recv(4)                                                                       
            sockLen = int.from_bytes(length, 'little')          
            sockIntLen = socket.ntohl(sockLen)
            message = length + listenSock.recv(sockIntLen)

            try:
                print(f'[PROXY]received {who}: ' + str(message.decode()))
            except:
                print(f'[PROXY]received {who}: couldn\'t decode')

            threadSend = threading.Thread(target=self.sendTo,args=(sendSock,message,))
            threadSend.start()