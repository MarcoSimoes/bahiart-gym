import socket
import sys
import sexpr

class Parser(object):

    sexp = None

    def __init__(self, sock: socket):
        
        self.socket = sock


    def parse(self, string:str):
        
        self.parsedExp = sexpr.str2sexpr(string)


    def search(self,word: str, lst: list):
        for i in range(0,len(lst)):
            if type(lst[i]) is list:
                self.search(word, lst[i])
            elif lst[i] == word:
                print(word, '=', lst[i+1])
            else:
                return

    def getValue(self, word: str, lst: list):
        for i in range(0,len(lst)):
            if type(lst[i]) is list:
                self.search(word, lst[i])
            elif lst[i] == word:
                return lst[i+1]
            else:
                return


# DEBUG SEARCH
# def testSearch(lst: list):
#     #print("list length:", len(lst))
#     for i in range(0, len(lst)):
#         #print(type(lst[i]) is list)
#         if type(lst[i]) is list:
#             testSearch(lst[i])
#         elif lst[i] == 'FieldWidth':
#             print(lst[i+1])
