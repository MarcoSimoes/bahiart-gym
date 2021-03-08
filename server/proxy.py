import socket
import threading

class Proxy:

    # Variable to be passed to the parser
    self.serverToAgent = ''

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

    def connectNewAgent(self):
        self.agentSock.listen()
        newAgentSock, _ = self.agentSock.accept()
        print("[PROXY]new agent connected")
        return newAgentSock

    def start(self):
        # '''
        # STARTS THE PROXY
        # '''
        while True:
            newAgentSock = self.connectNewAgent()
            try:
                self.connectToServer()
            except:
                pass

            connectionAgentToServer = threading.Thread(target=self.connectionManager,args=(newAgentSock,self.serverSock,str('agent')))   
            connectionServerToAgent = threading.Thread(target=self.connectionManager,args=(self.serverSock,newAgentSock,str('server')))
            
            connectionAgentToServer.start()
            connectionServerToAgent.start()  

    def connectionManager(self,listenSock,sendSock,whoIsSending):
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
            message = listenSock.recv(sockIntLen)
            if whoIsSending == 'server':
                # print("SERVER SENDING : " + message.decode())
                self.serverToAgent = message.decode()

            # if whoIsSending == 'agent':
            #     print("AGENT SENDING  : " + message.decode())
            message = length + message
            sendSock.sendall(message)