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
                if lst[i] == 'HJ':
                    hingeName = lst[i+1]
                    if hingeName[1] == word:
                        ax = lst[i+2]
                        value = ax[1]
                        return value
                    else:
                        continue
                elif type(lst[i]) is list:
                    value = self.getHinjePos(word, lst[i], old)
                else:
                    continue
                if value == None or value == old:
                    continue
            else:
                return value
        if value is None:
            value = old
        return value

    #Can be used for ACC too. Just send 'ACC' as the word instead of 'GYR'
    def getGyr(self, word: str, lst: list, old):
        value = []
        for i in range(0,len(lst)):
            if value == [] or value == old:
                if lst[i] == word:
                    valuesList = lst[i+2]
                    x = valuesList[1]
                    y = valuesList[2]
                    z = valuesList[3]
                    value = [x,y,z]
                    return value
                elif type(lst[i]) is list:
                    value = self.getGyr(word, lst[i], old)
                else:
                    continue
                if value == None or value == old:
                    continue
            else:
                return value
        if value is None:
            value = old
        return value