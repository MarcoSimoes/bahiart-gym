import subprocess as proc
import socket
import sys
import sexpr
import parser
import trainer
#from connection import sParser, comand, Conection


HOST = 'localhost'
PORT = 3200
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))

comand = trainer.Trainer(sock)
sParser = parser.Parser(sock)

while True:
    sParser.search('time', sParser.sexp)
