import socket
import sys
import sexpr
import proxy
import comms
from parsr import Parser
from singleton import Singleton

class ServerParser(Parser, Singleton):
    """
    Class to retrieve and parse the S-Expression sent from the server
    'Consider changing the name to TrainerParser'
    """

    def __init__(self):
        self.socket = comms.Comms.serverSocket
    pass