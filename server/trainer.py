from server.comms import Comms
from server.singleton import Singleton
#from connection import sock

class Trainer(Singleton):
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
        self.net = Comms()

    def changePlayMode(self, playmode: str):
        
        self.msg = "(playMode " + playmode + ")"                              
        self.net.send(self.msg)

    def beamBall(self, x, y, z):
        self.msg = "(ball (pos " + str(x) + " " + str(y) + " " + str(z) + "))"
        self.net.send(self.msg)

    def beamPlayer(self, unum, team, x, y, z=0.3):
        self.msg = "(agent (unum " + str(unum) + ")(team " + team + ")(pos " + str(x) + " " + str(y) + " " + str(z) + "))"
        self.net.send(self.msg)