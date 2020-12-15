import subprocess as proc
import socket
import sys
import sexpr
#from connection import sock

class Trainer:

    def __init__(self, sock: socket):
        self.socket = sock

    # Cabem melhorias na hora de fazer uma interface, 
    # como facilitar essa troca de playmode por uma caixa de opções 
    # para não ter erro de digitação.
    def changePlayMode(self, playmode: str):
        
        #Constroi a mensagem
        msg = "(playMode " + playmode + ")"                              
        
        # Pega o tamanho da mensagem e traduz utilizando 
        # o metodo Host To Network Long
        msgLen = socket.htonl(len(msg))                                 
        
        # Converte o tamanho de inteiro para bytes no formato little, 
        # assim como é devolvido pelo servidor.
        prefix = msgLen.to_bytes(4, 'little')                           

        # Concatena o prefixo com a mensagem, 
        # transformando o prefixo em string com encode em utf-8, 
        # evitando duplicação do "b" de mensagens em bytes
        fullmsg = str(prefix, "utf-8") + msg                            

        # Encoda a mensagem e envia ela pelo socket TCP
        self.socket.send(fullmsg.encode())


    def beamBall(self, x: float, y: float, z:float):
        msg = "(ball (pos " + x + " " + y + " " + z + "))"
        msgLen = socket.htonl(len(msg))
        prefix = msgLen.to_bytes(4, 'little')
        fullmsg = str(prefix, "utf-8") + msg
        self.socket.send(fullmsg.encode())

    def beamPlayer(self, team: str, unum: int, x: float, y: float, z: float):
        msg = "(agent (team " + team + ")(unum " + unum + ")(pos " + x + " " + y + " " + z + "))"
        msgLen = socket.htonl(len(msg))
        prefix = msgLen.to_bytes(4, 'little')
        fullmsg = str(prefix, "utf-8") + msg
        self.socket.send(fullmsg.encode())