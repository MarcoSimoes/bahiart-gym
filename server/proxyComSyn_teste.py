import socket
import threading
import time
from multiprocessing import Process

globau = False
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


    def send(self,age,serv,f):
        global globau
        length = age.recv(4)                                                                       
        sockLen = int.from_bytes(length, 'little')          
        sockIntLen = socket.ntohl(sockLen)
        message = age.recv(sockIntLen)
        message = length + message
        serv.sendall(message)
        globau = True
        try:
            f.write("[AGENT]" + str(message.decode()))
        except:
            try:
                f.write("[AGENT]" + message.decode())
            except:
                f.write("[AGENT]COULDN'T DECODE")
        f.write('\n')
        f.write('\n')

    def connectionManager(self,agentSock,serverSock):
        # '''
        # Manage 2 connections.
        # Receives from X and sends to Y
        # '''

        # Initializing variable
        message = ''.encode() 

        # 
        global globau
        f = open("teste.txt", "a")
        # 
        a = time.time()
        timer = True
        while True:
            if time.time() - a > 15:
                timer = False
            # AGENTE ENVIANDO MENSAGEM PARA SERVIDOR
            # length = agentSock.recv(4)                                                                       
            # sockLen = int.from_bytes(length, 'little')          
            # sockIntLen = socket.ntohl(sockLen)
            # message = agentSock.recv(sockIntLen)
            # message = length + message
            # serverSock.sendall(message)
            
            action_process = Process(target=self.send,args=(agentSock,serverSock,f,))
            action_process.start()
            action_process.join(timeout=0.1)
            action_process.terminate()
            if globau == False and timer:
                msg = '(syn)'
                msgLen = socket.htonl(len(msg))
                prefix = msgLen.to_bytes(4,'little')          
                message = prefix + msg.encode()
                serverSock.sendall(message) 
            else:
                globau = False
            


            
            # if not message:
                # agentSock.close()
                # serverSock.close()
                # # self.connectToServer()
                # print('[PROXY]Closed agent connection')

                # # 
                # f.close()
                # # 

                # return
            # 
            try:
                f.write("[AGENT]" + str(message.decode()))
            except:
                try:
                    f.write("[AGENT]" + message.decode())
                except:
                    f.write("[AGENT]COULDN'T DECODE")
            f.write('\n')
            f.write('\n')
            # 
            
            


            # SERVIDOR ENVIANDO MENSAGEM PARA AGENTE
            length = serverSock.recv(4)                                                                       
            sockLen = int.from_bytes(length, 'little')          
            sockIntLen = socket.ntohl(sockLen)
            message = serverSock.recv(sockIntLen)
            message = length + message
            agentSock.sendall(message)

            
            # 
            try:
                f.write("[SERVER]" + str(message.decode()))
            except:
                try:
                    f.write("[SERVER]" + message.decode())
                except:
                    f.write("[SERVER]" + str(message))     

            f.write('\n')      
            f.write('\n')
            # 

            