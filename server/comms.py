import subprocess as proc
import socket
import sys
from server import sexpr
import trainer
from server import parsr


class Comms(object):
    """
    Communication class between Gym and Server.
    Constructor default parameters creates a HOST-PORT localhost-3200 connection
    """

    _instance = None
    
    def __new__(cls):
        if not cls._instance:
            cls._instance = super(Comms, cls).__new__(cls)
        return cls._instance

    def __init__(self, host='localhost', port=3200):

        self.HOST = host
        self.PORT = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((self.HOST, self.PORT))
        self.setParser()



    def setParser(self):
        self.sParser = parsr.Parser(self.sock)

    def send(self, msg: str):
        """
        Sends trainer message to server.
        """
        msgLen = socket.htonl(len(msg))
        prefix = msgLen.to_bytes(4, 'little')
        fullmsg = str(prefix, "utf-8") + msg
        self.sock.send(fullmsg.encode())

    def updateSExp(self):
        # Receive 4 first bytes which contains message lenght info
        lenght = self.sock.recv(4)                                                               
        
        # Converts message bytes into integer, 
        # with the bytes ordered from lowest to highest(little)
        sockLen = int.from_bytes(lenght, 'little')          
        
        # Converts message lenght from 'network' to 'host long'(NtoHL) 
        sockIntLen = socket.ntohl(sockLen)

        # Receive message with the right size as parameter
        byteMsg = self.sock.recv(sockIntLen)

        #Transforms byteMsg into string
        self.sexp = str(byteMsg, 'utf-8')

        #Sends string with the S-Expression to the parser
        self.sParser.parse(self.sexp)