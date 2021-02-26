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

    def start(self):
        # '''
        # STARTS THE PROXY
        # '''
        while True:
            print('[PROXY]Waiting agent to connect on port : ' + str(self.AGENT_PORT))
            self.agentSock.listen()
            newAgentSock, _ = self.agentSock.accept()
            threadNewConnection = threading.Thread(target=self.connectNewAgents,args=(newAgentSock,))
            threadNewConnection.start()
        
        

    def connectNewAgents(self,newAgentSock):
        # '''
        # Get new agent to connect
        # '''
        print('[PROXY]new agent connected')
        while True:
            self.connectToServer()

            connectionAgentToServer = threading.Thread(target=self.connectionManager,args=(newAgentSock,self.serverSock,'[AGENT - SERVER]'))
            connectionServerToAgent = threading.Thread(target=self.connectionManager,args=(self.serverSock,newAgentSock,'[SERVER - AGENT]'))

            connectionAgentToServer.start()
            connectionServerToAgent.start()
 

    # MUST NOT CALL // PRIVATE
    def sendTo(self,sock,message):
        # '''
        # Send message to socket
        # '''
        # print("SENT")
        # print(message.decode)
        sock.sendall(message)

    # MUST NOT CALL // PRIVATE
    def connectionManager(self,listenSock,sendSock,who):
        # '''
        # Manage 2 connections.
        # Receives from X and sends to Y
        # '''

        # Initializing variable
        message = ''.encode() 
        while True:
            length = listenSock.recv(4)                                                                       
            sockLen = int.from_bytes(length, 'little')          
            sockIntLen = socket.ntohl(sockLen)
            message = length + listenSock.recv(sockIntLen)

            # try:
            #     print(f'[PROXY]received {who}: ' + str(message.decode()))
            # except:
            #     print(f'[PROXY]received {who}: couldn\'t decode')

            threadSend = threading.Thread(target=self.sendTo,args=(sendSock,message,))
            threadSend.start()
