import socket
import threading

class Proxy:

    def __init__(self,agent_port,server_port=3100,server_host='localhost'):
        # '''
        # INITIALIZES THE SERVER_HOST, SERVER_PORT, AGENT_PORT AND ALSO 
        # DOES THE INITIAL SET UP FOR THE AGENT SOCKET AND SERVER SOCKET
        # '''

        self.SERVER_HOST = server_host
        self.SERVER_PORT = server_port
        self.AGENT_PORT = agent_port


        # AGENT SOCKET SETUP
        # Creates a 'server' to receive the agent's messages
        self.agentSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.agentSock.bind((self.SERVER_HOST, self.AGENT_PORT))

        


    def connectToServer(self):
        # '''
        # ESTABLISH CONNECTION WITH THE RCSSSERVER3D
        # '''

        # SERVER SOCKET SETUP
        self.serverSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        self.serverSock.connect((self.SERVER_HOST, self.SERVER_PORT))
        print("[PROXY] Connected to server on port : " + str(self.SERVER_PORT))


    def start(self):
        # '''
        # STARTS THE PROXY
        # '''
        while True:
            # Listening until the agent starts the connection
            self.agentSock.listen()
            newAgentSock, _ = self.agentSock.accept()

            try:
                # CONNECTING TO RCSSSERVER
                # If there's any problem in the connection 
                # the proxy will try to connect again when the next agent enter
                self.connectToServer()
            except:
                pass

            try:
                # CREATE NEW THREADS TO MANAGE THE CONNECTION
                self.connectionManager(newAgentSock,self.serverSock)
                print("[PROXY] New agent connected on port : " + str(self.AGENT_PORT))
            except:
                print("[PROXY] Couldn't connect new agent.")


    def connectionManager(self,agentSock,serverSock):
        # '''
        # MANAGES THE CONNECTION OF A NEW AGENT BY CREATING 
        # A THREAD TO SEND MESSAGES FROM THE AGENT TO THE 
        # SERVER AND ANOTHER ONE TO SEND MESSAGES FROM THE 
        # SERVER TO THE AGENT
        # '''

        threading._start_new_thread(self.sender,(agentSock,serverSock))
        threading._start_new_thread(self.sender,(serverSock,agentSock))


    def sender(self,receiveSock,sendSock):
        # ''' 
        # SEND MESSAGES FROM receiveSock TO sendSock AND 
        # CLOSES THE CONNECTION IF IT'S BROKEN
        # '''

        message = ''.encode() 
        fullmessage = ''.encode

        while True:
             # RECEIVING MESSAGE
            try:
                length = receiveSock.recv(4)
            except:
                # CLOSING THE CONNECTION IF IT'S BROKEN 
                receiveSock.close()
                print('[PROXY] Closed connection.')
                return                                

            sockLen = int.from_bytes(length, 'little')          
            sockIntLen = socket.ntohl(sockLen)
            message = receiveSock.recv(sockIntLen)
            fullmessage = length + message

            # if not message:
            #     receiveSock.close()
            #     # self.connectToServer()
            #     print('[PROXY]Closed connection.')
            #     # f.close()
            #     return

            try:
                sendSock.sendall(fullmessage)
            except:
                # CLOSING THE CONNECTION IF IT'S BROKEN 
                receiveSock.close()
                print('[PROXY] Closed connection.')
                return


        #     # DEBUG MESSAGES

        #     # > If needed, the message can be transformed into string 
        #     # using message.decode()
        #     # Ex:
        #     # print(message.decode)

        #     # > It's important to not use the full message, because 
        #     # sometimes the decode method can't decode the initial 
        #     # 4 bytes which contains the size of the message.

        #     # > If the length(4 first bytes) is needed i recommend you to use 
        #     # try and except to catch any errors, because sometimes, 
        #     # as i said before, the decode method can't decode the 
        #     # initial bytes to string.

        #     # Ex:
        #     # try:
        #     #   print(fullMessage.decode())
        #     # except:
        #     #   print("Couldn't decode the message.")