import subprocess as proc
import socket
import sys
import sexpr
import parser
import trainer
import comms
#from connection import sParser, comand, Conection


net = comms.Comms()

comand = trainer.Trainer(net.sock)

tempo = net.sParser.getValue('time', net.sParser.sexp)
print(tempo)