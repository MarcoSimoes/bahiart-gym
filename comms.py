import subprocess as proc
import socket
import sys
import sexpr
import trainer
import parsr


class Comms(object):

    _instance = None
    
    def __new__(self):
        if not self._instance:
            self._instance = super(Comms, self).__new__(self)
        return self._instance

    HOST = 'localhost'
    PORT = 3200
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((HOST, PORT))
    sParser = parsr.Parser(sock)
    
    while True:
        sParser.updateSexp()