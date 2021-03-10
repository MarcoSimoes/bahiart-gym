import socket
import threading

class Proxy:

    def __init__(self,agent_port,server_port=3100,server_host='localhost'):

        self.SERVER_HOST = server_host
        self.SERVER_PORT = server_port
        self.AGENT_PORT = agent_port

        # AGENT CONNECTION INITIAL SETUP
        self.agentSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.agentSock.bind((self.SERVER_HOST, self.AGENT_PORT))
        

    def connectToServer(self):
        # SERVER CONNECTION INITIAL SETUP
        self.serverSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.serverSock.connect((self.SERVER_HOST, self.SERVER_PORT))
        print("[PROXY]Connected to server on port : " + str(self.SERVER_PORT))

    def start(self):
        # '''
        # STARTS THE PROXY
        # '''
        while True:
            self.agentSock.listen()
            newAgentSock, _ = self.agentSock.accept()
            print("[PROXY]new agent connected")

            try:
                self.connectToServer()
            except:
                pass

            try:
                threading._start_new_thread(self.connectionManager,(newAgentSock,self.serverSock))
            except:
                pass
            return

    def connectionManager(self,agentSock,serverSock):
        # '''
        # Manage 2 connections.
        # Receives from X and sends to Y
        # '''

        # Initializing variable
        message = ''.encode() 
        while True:
            message = ''.encode() 
            # AGENTE ENVIANDO MENSAGEM PARA SERVIDOR
            length = agentSock.recv(4)                                                                       
            sockLen = int.from_bytes(length, 'little')          
            sockIntLen = socket.ntohl(sockLen)
            message = agentSock.recv(sockIntLen)
            message = length + message

            if not message:
                agentSock.close()
                serverSock.close()
                print('[PROXY]Closed agent connection')
                return
            serverSock.sendall(message)

            # SERVIDOR ENVIANDO MENSAGEM PARA AGENTE
            length = serverSock.recv(4)                                                                       
            sockLen = int.from_bytes(length, 'little')          
            sockIntLen = socket.ntohl(sockLen)
            message = serverSock.recv(sockIntLen)
            message = length + message
            agentSock.sendall(message)