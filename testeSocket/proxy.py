import socket
# import sexpr
# import trainer # Acredito q n será necessário ter o trainer aq mano
# Tirei só pra fazer uns testes.
# import parsr # Tirei o 'from server' pq tá na mesma pasta

class Proxy(object):
    """
    Proxy class to send and receive agent messages.
    It simply serves as a simple gateway between the team
    and the server while retrieving the necessary data.
    """

    _instance = None
    agentMessage = None
    serverMessage = None
    
    def __new__(cls):
        if not cls._instance:
            cls._instance = super(Proxy, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        print()
        # self.start_serverSock()
        # self.start_agentSock()
        # self.setProxyParser()


    def start_serverSock(self):
        self.serverHOST = 'localhost'
        self.serverPORT = 3400
        try:
            self.serverSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            print("Server socket created")
        except socket.error as err:
            print("Server socket not created.")
            print("Error : " + str(err))

        try:
            self.serverSock.connect((self.serverHOST, self.serverPORT))
            print("Server socket connected.")
        except socket.error as err:
            print("Server socket not connected.")
            print("Error : " + str(err))

    def start_agentSock(self):
        self.agentProxyAddress = ('localhost', 3300)
        try:
            self.agentSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            print("Client socket created.")
        except socket.error as err:
            print("Client socket not created.")
            print("Error : " + str(err))
        
        self.agentSock.bind(self.agentProxyAddress)
        self.agentSock.listen()
        print('Waiting agent to connect...')
        self.agentConnection, _ = self.agentSock.accept()
        print('Agent connected')
        
    def setProxyParser(self):
        self.proxyParser = parsr.Parser(self.serverSock)

    def receiveAgentMessage(self):
        self.msgAgent = self.agentConnection.recv(1024)
        # while True:
        #     partialMsg = self.agentConnection.recv(4)
        #     if len(partialMsg) <= 0:
        #         break
        #     self.msgAgent += partialMsg
        
        # lenght = self.agentSock.recv(4)                                                                       
        # sockLen = int.from_bytes(lenght, 'little')          
        # sockIntLen = socket.ntohl(sockLen)
        # byteMsg = self.agentSock.recv(sockIntLen)

        # self.agentMessage = str(byteMsg, 'utf-8')

    def forwardAgentMessage(self):
        self.serverSock.sendall(self.msgAgent)
        
        # self.agentMessage = self.agentMessage + '(syn)'
        
        # msgLen = socket.htonl(len(self.agentMessage))
        # prefix = msgLen.to_bytes(4, 'little')
        # fullmsg = str(prefix, "utf-8") + self.agentMessage
        
        # self.serverSock.send(self.agentMessage.encode())

    def receiveServerMessage(self):
        self.msgServer = self.serverSock.recv(1024)
        # while True:
        #     partialMsg = self.serverSock.recv(4)
        #     if len(partialMsg) <= 0:
        #         break
        #     self.msgServer += partialMsg

        # lenght = self.serverSock.recv(4)                                                                       
        # sockLen = int.from_bytes(lenght, 'little')          
        # sockIntLen = socket.ntohl(sockLen)
        # byteMsg = self.serverSock.recv(sockIntLen)

        # self.serverMessage = str(byteMsg, 'utf-8')

    def forwardServerMessage(self):
        self.agentConnection.sendall(self.msgServer)
        
        # msgLen = socket.htonl(len(self.serverMessage))
        # prefix = msgLen.to_bytes(4, 'little')
        # fullmsg = str(prefix, "utf-8") + self.serverMessage

        # self.agentSock.send(self.serverMessage.encode())

    def run(self):
        self.setProxyParser()
        self.agentSock.listen()
        agentConn, agentAddr = self.agentSock.accept()
        while True:
            self.receiveAgentMessage()
            self.forwardAgentMessage()
            self.receiveServerMessage()
            self.proxyParser.parse(self.serverMessage)
            self.forwardServerMessage()