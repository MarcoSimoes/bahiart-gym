import socket
import threading
import sys

class Proxy:


    def __init__(self,agent_port,server_port=3100,server_host='localhost'):
    # def __init__(self,agent_port,server_port=3300,server_host='localhost'):
        self.SERVER_HOST = server_host
        self.SERVER_PORT = server_port
        self.AGENT_PORT = agent_port
        self.FILE = 'agent'
        self.agentNumber = int(1)


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

                self.connectionManager(newAgentSock,self.serverSock)
            except:
                pass
    


    def connectionManager(self,agentSock,serverSock):
        threading._start_new_thread(self.sender,(agentSock,serverSock,'[AGENT]',self.agentNumber))
        threading._start_new_thread(self.sender,(serverSock,agentSock,'[SERVER]',self.agentNumber))
        self.agentNumber += 1

    def sender(self,agentSock,serverSock,who,agentNumber):
        message = ''.encode() 
        fullmessage = ''.encode
        # f = open(str(self.FILE + str(agentNumber)), "a")
        while True:
            # AGENTE ENVIANDO MENSAGEM PARA SERVIDOR
            try:
                length = agentSock.recv(4)
            except:
                # f.write('[PROXY]' + '-' + 'Couldnt receive message from' + who + '('+who+' se desconectou)' + '\n\n')   
                agentSock.close()
                return                                                                 
            sockLen = int.from_bytes(length, 'little')          
            sockIntLen = socket.ntohl(sockLen)
            message = agentSock.recv(sockIntLen)
            fullmessage = length + message

            if not message:
                agentSock.close()
                # self.connectToServer()
                print('[PROXY]Closed agent connection')
                # f.close()
                return
            try:
                serverSock.sendall(fullmessage)
                # f.write(who + '-' + message.decode() + '\n\n')
            except:
                if(who == '[AGENT]'):
                    pass
                    # f.write('[PROXY]' + '-' + 'Couldnt send message to SERVER(servidor se desconectou)' + '\n\n')
                else:
                    # f.write('[PROXY]' + '-' + 'Couldnt send message to AGENT(agente se desconectou)' + '\n\n')
                    pass
                agentSock.close()
                # self.connectToServer()
                # f.close()
                return
            

