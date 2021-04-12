import socket
import sys
from server import sexpr
from server import proxy
from server import comms
from server.parsr import Parser
from server.singleton import Singleton

class ServerParser(Parser, Singleton):
    """
    Class to retrieve and parse the S-Expression sent from the server
    'Consider changing the name to TrainerParser'
    """

    def __init__(self):
        self.socket = comms.Comms.serverSocket
    pass