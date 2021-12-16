import socket
from server.singleton import Singleton

class InvalidHostAndPortLengths(Exception):
    """ Raised when Host and Port lists has different sizes """
    pass

class AgentComms(Singleton):
    """
    Communication class between Gym and Agents.
    Constructor default parameters creates a HOST-PORT localhost-3200 connection
    """
    

    def __init__(self, host=['localhost'], port=[4100]):

        if len(host)!=len(port):
            raise InvalidHostAndPortLengths("Host and Port lists should have the same size!")
        self.HOST = host
        self.PORT = port
        self.socks=[]
        i=1
        try: 
            for h in host:
                sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.socks.append(sock)             
                print("Socket {} created".format(i))
                i=i+1
        except socket.error as err:
            print("Socket {} not created.".format(i))
            print("Error : " + str(err))
        
        i=1
        try: 
            
            for h,p,s in zip(host,port,self.socks):
                s.connect((h, p))
              
                print("[AGENTCOMMS]Connection {} established".format(i))
                i+=1
 #               s.setblocking(0)
        except socket.error as err:
            print("[AGENTCOMMS]Connection {} not established.".format(i))
            print("Error : " + str(err))



    def sendAll(self, msg: str):
        """
        Sends environment message msg to all agents.
        """
        msgLen = socket.htonl(len(msg))
        prefix = msgLen.to_bytes(4, 'little')
        fullmsg = str(prefix, "utf-8") + msg
        i=1
        try:
           for s in self.socks:
                s.sendall(fullmsg.encode())
                print("[AGENTCOMMS]Socket message {} sent.".format(i))
                print("[AGENTCOMMS]Socket message: {}".format(fullmsg))
                i+=1
        except socket.error as err:
            print("[AGENTCOMMS]Socket message {} not sent.".format(i))
            print("Error : " + str(err))
            print("Message : " + str(fullmsg))

    def send(self, index: int, msg:str):     
       """
       Sends the message msg to the agent identified by the socket in the position "index" in the list of sockets initialized in this object.
       
       Parameters
       ----------
       index : int
           position of the socket in the sockets list to which the message will be sent.
       msg : str
            Message to be sent.
        
        Returns
        -------
        None.
        
        """
       msgLen = socket.htonl(len(msg))
       prefix = msgLen.to_bytes(4, 'little')
       fullmsg = str(prefix, "utf-8") + msg
       sock=self.socks[index]
       try:
           sock.sendall(fullmsg.encode())    
           print("[AGENTCOMMS]Socket message sent.")
       except socket.error as err:
           print("[AGENTCOMMS]Socket message not sent.")
           print("Error : " + str(err))
           print("Message : " + str(fullmsg))
        
    def receiveAll(self):
        i=1
        try:
            for s in self.socks:
                s.recv(4096)
                print("[AGENTCOMMS]Socket message {} received".format(i))
                i+=1
        except socket.error as err:
            print("[AGENTCOMMS]Socket message {} not received".format(i))
            print("Error : " + str(err))
                  
    def receive(self,index: int):
            try:
                self.socks[index].recv(4096)
                print("[AGENTCOMMS]Socket message received.")
            except socket.error as err:
                print("[AGENTCOMMS]Socket message not received.")
                print("Error : " + str(err))
                