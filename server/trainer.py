import sys
import sexpr
import comms
#from connection import sock

class Trainer:
    """
    Sends comands to the server as a Trainer program.

    Example:

    # Builds the message
        msg = "(playMode " + playmode + ")"                              

    # Get message length and translate using "Host To Network Long" method. 
        msgLen = socket.htonl(len(msg))                                 
    
    # Converts integer size to bytes in the format 'little', 
    # in the same way it's returned from the server.
        prefix = msgLen.to_bytes(4, 'little')                           

    # Concatenates the prefix with the message,
    # turning the prefix into string(with 'utf-8' encode),
    # avoiding duplication of "b" in byte messages.
        fullmsg = str(prefix, "utf-8") + msg                            

    # Encodes the message and sends it through TCP socket 
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