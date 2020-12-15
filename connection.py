""" 
import subprocess as proc
import socket
import sys
import sexpr
import parser
import trainer


class Conection:

    def __init__(self, host: str, port: int):
        self.HOST = host
        self.PORT = port
        # HOST = 'localhost'
        # PORT = 3200
        
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((HOST, PORT))

    comand = trainer.Trainer(sock)
    sParser = parser.Parser(sock) """