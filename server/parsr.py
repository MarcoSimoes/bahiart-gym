import socket
import sys
from server import sexpr

class Parser(object):
    """
    Class to parse S-Expression from server
    """
    result = None

    # def __new__(cls):
    #     if not cls._instance:
    #         cls._instance = super(Parser, cls).__new__(cls)
            
    #     return cls._instance

    def __init__(self, sock: socket):
        
        self.socket = sock


    def parse(self, string:str):
        
        self.parsedExp = sexpr.str2sexpr(string)


    def search(self, word: str, lst: list):
        for i in range(0,len(lst)):
            if type(lst[i]) is list:
                self.search(word, lst[i])
            elif lst[i] == word:
                print(word, '=', lst[i+1])
            continue
        return

    def getValue(self, word: str, lst: list, old):
        value = None
        for i in range(0,len(lst)):
            if value == None or value == old:
                if lst[i] == word:
                    value = lst[i+1]
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