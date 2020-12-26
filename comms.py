import subprocess as proc
import socket
import sys
import sexpr
import trainer
import parsr


class Comms(object):
    """
    Classe de comunicação entre o Gym e o servidor. Parâmetros padrões do método construtor da classe
    levam a uma conexão HOST-PORT localhost-3200.
    """

    _instance = None
    
    def __new__(self):
        if not self._instance:
            self._instance = super(Comms, self).__new__(self)
        return self._instance

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
        #Recebe os primeiros 4 bytes que dizem respeito ao tamanho da mensagem
        lenght = self.sock.recv(4)                                                               
        
        # Converte os bytes da mensagem em inteiro, 
        # com os bytes ordenados do menor para o maior (little)
        sockLen = int.from_bytes(lenght, 'little')          
        
        #Converte o tamanho da mensagem de network para host long (NtoHL)
        sockIntLen = socket.ntohl(sockLen)

        #Recebe a mensagem com o tamanho correto passado como parâmetro
        byteMsg = self.sock.recv(sockIntLen)

        #Transforms byteMsg into string
        self.sexp = str(byteMsg, 'utf-8')

        #Sends string with the S-Expression to the parser
        self.sParser.parse(self.sexp)