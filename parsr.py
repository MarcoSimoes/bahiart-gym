import socket
import sys
import sexpr

class Parser(object):
    """
    Class to parse S-Expression from server
    """
    result = None

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
        return

    def getValue(self, word: str, lst: list):
        for i in range(0,len(lst)):
            if type(lst[i]) is list:
                self.result = self.getValue(word, lst[i])
            elif lst[i] == word:
                return lst[i+1]
            return self.result
        return self.result