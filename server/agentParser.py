import socket
import sys
import sexpr
import proxy
from parsr import Parser

class AgentParser(Parser):
    """
    Class to retrieve and parse the S-Expression sent by the server to the agents
    """
    result = None

    def __init__(self):
        pass

    def getHinjePos(self, word: str, lst: list, old):
        value = None
        for i in range(0,len(lst)):
            if value == None or value == old:
                if lst[i] == word:
                    value = lst[i+4]
                    return value
                elif type(lst[i]) is list:
                    value = self.getValue(word, lst[i], old)
                else:
                    continue
                if value == None or value == old:
                    continue
            else:
                return value
        if value is None:
            value = old
        return value