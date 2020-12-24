import sys
import sexpr
import comms
#from connection import sock

class Trainer:
    """
    Sends comands to the server as a Trainer program.

    Example:

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

    """

    def __init__(self):
        self.net = comms.Comms()

    def changePlayMode(self, playmode: str):
        
        self.msg = "(playMode " + playmode + ")"                              
        self.net.send(self.msg)

    def beamBall(self, x: float, y: float, z:float):
        self.msg = "(ball (pos " + x + " " + y + " " + z + "))"
        self.net.send(self.msg)

    def beamPlayer(self, team: str, unum: int, x: float, y: float, z: float):
        self.msg = "(agent (team " + team + ")(unum " + unum + ")(pos " + x + " " + y + " " + z + "))"
        self.net.send(self.msg)