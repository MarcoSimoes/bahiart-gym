import socket
import threading

class agentProxy:

    def __init__(self,agentSock,server_port=3100,server_host='localhost'):
        self.SERVER_HOST = server_host
        self.SERVER_PORT = server_port
        self.agentSock = agentSock
        self.isConnected = True

    def connectToServer(self):
        serverSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        serverSock.connect((self.SERVER_HOST, self.SERVER_PORT))
        return serverSock

    def closeConnection(self):
        try:
            try:
                self.serverSock.shutdown(socket.SHUT_RDWR)
            except:
                pass
            try:
                self.agentSock.shutdown(socket.SHUT_RDWR)
            except:
                pass
        except:
            pass
        finally:
            print("Closed connection")
            self.isConnected = False
            return
        

    def connectionManager(self):
        self.serverSock = self.connectToServer()
        threading._start_new_thread(self.serverToAgent,())
        threading._start_new_thread(self.agentToServer,())

    def serverToAgent(self):
        while True:
            try:
                length = self.serverSock.recv(4)
            except:
                if not self.isConnected:
                    return

            sockLen = int.from_bytes(length, 'little')          
            sockIntLen = socket.ntohl(sockLen)

            try:
                message = self.serverSock.recv(sockIntLen)
            except:
                if not self.isConnected:
                    return

            if not message:
                if self.isConnected:
                    self.closeConnection()
                    return

            fullmessage = length + message

            try:
                self.agentSock.sendall(fullmessage)
            except:
                if not self.isConnected:
                    return
                else:
                    self.serverSock = self.connectToServer()

    def agentToServer(self):
        while True:
            try:
                length = self.agentSock.recv(4)
            except:
                if not self.isConnected:
                    return

            sockLen = int.from_bytes(length, 'little')          
            sockIntLen = socket.ntohl(sockLen)

            try:
                message = self.agentSock.recv(sockIntLen)
            except:
                if not self.isConnected:
                    return

            if not message:
                if self.isConnected:
                    self.closeConnection()
                    return

            fullmessage = length + message

            try:
                self.serverSock.sendall(fullmessage)
            except:
                if not self.isConnected:
                    return
                else:
                    self.serverSock = self.connectToServer()