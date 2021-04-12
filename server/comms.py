import socket
import sys
from server import sexpr
from server import trainer
from server import serverParser
from server.singleton import Singleton

class Comms(Singleton):
    """
    Communication class between Gym and Server.
    Constructor default parameters creates a HOST-PORT localhost-3200 connection
    """
    serverSocket = None

    def __init__(self, host='localhost', port=3200):

        self.HOST = host
        self.PORT = port
        try: 
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            print("Socket created.")
        except socket.error as err:
            print("Socket not created.")
            print("Error : " + str(err))
        
        try: 
            self.sock.connect((self.HOST, self.PORT))
            self.serverSocket = self.sock
            print("Connection established")
        except socket.error as err:
            print("Connection not established.")
            print("Error : " + str(err))

        self.setParser()



    def setParser(self):
        self.sParser = serverParser.ServerParser()

    def send(self, msg: str):
        """
        Sends trainer message to server.
        """
        msgLen = socket.htonl(len(msg))
        prefix = msgLen.to_bytes(4, 'little')
        fullmsg = str(prefix, "utf-8") + msg
        try:
            self.sock.send(fullmsg.encode())
            print("Socket message sent.")
        except socket.error as err:
            print("Socket message not sent.")
            print("Error : " + str(err))
            print("Message : " + str(fullmsg))

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