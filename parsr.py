import socket
import sys
import sexpr

class Parser(object):
    """
    Class to parse S-Expression from server
    """

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
            else:
                return


    #Não retorna valor algum. Sempre None. Verificar e corrigir.
    def getValue(self, word: str, lst: list):
        for i in range(0,len(lst)):
            if type(lst[i]) is list:
                self.getValue(word, lst[i])
            elif lst[i] == word:
                self.result = lst[i+1]
                return self.result
            else:
                self.result = 'not found'
                return self.result