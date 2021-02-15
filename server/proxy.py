import socket
from server import sexpr
import trainer
from server import parsr

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

        self.start_serverSock()
        self.start_agentSock()
        self.setProxyParser()


    def start_serverSock(self):
        self.serverHOST = 'localhost'
        self.serverPORT = 3100
        try:
            self.serverSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            print("Socket created")
        except socket.error ass err:
            print("Socket not created.")
            print("Error : " str(err))

        try:
            self.serverSock.connect((self.serverHOST, self.serverPORT))
            print("Socket connected.")
        except socket.error as err:
            print("Socket not connected.")
            print("Error : " + str(err))

    def start_agentSock(self):
        self.agentProxyAddress = ('localhost', 3500)
        self.agentSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.agentSock.bind(self.agentProxyAddress)

    def setProxyParser(self):
        self.proxyParser = parsr.Parser(self.serverSock)

    def receiveAgentMessage(self):
        lenght = self.agentSock.recv(4)                                                                       
        sockLen = int.from_bytes(lenght, 'little')          
        sockIntLen = socket.ntohl(sockLen)
        byteMsg = self.agentSock.recv(sockIntLen)

        self.agentMessage = str(byteMsg, 'utf-8')

    def forwardAgentMessage(self):
        self.agentMessage = self.agentMessage + '(syn)'
        
        msgLen = socket.htonl(len(self.agentMessage))
        prefix = msgLen.to_bytes(4, 'little')
        fullmsg = str(prefix, "utf-8") + self.agentMessage
        
        self.serverSock.send(self.agentMessage.encode())

    def receiveServerMessage(self):
        lenght = self.serverSock.recv(4)                                                                       
        sockLen = int.from_bytes(lenght, 'little')          
        sockIntLen = socket.ntohl(sockLen)
        byteMsg = self.serverSock.recv(sockIntLen)

        self.serverMessage = str(byteMsg, 'utf-8')

    def forwardServerMessage(self):
        msgLen = socket.htonl(len(self.serverMessage))
        prefix = msgLen.to_bytes(4, 'little')
        fullmsg = str(prefix, "utf-8") + self.serverMessage

        self.agentSock.send(self.serverMessage.encode())

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