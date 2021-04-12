import socket
import sys
import sexpr
import proxy
from parsr import Parser
from singleton import Singleton

class ServerParser(Parser, Singleton):
    """
    Class to retrieve and parse the S-Expression sent from the server
    'Consider changing the name to TrainerParser'
    """
    
    pass