import subprocess as proc
import socket
import sys
import sexpr

class Parser:

    sexp = None

    def __init__(self, sock: socket):
        
        self.socket = sock


    def updateSexp(self):
        #Recebe os primeiros 4 bytes que dizem respeito ao tamanho da mensagem
        lenght = self.socket.recv(4)                                                               
        
        # Converte os bytes da mensagem em inteiro, 
        # com os bytes ordenados do menor para o maior (little)
        sockLen = int.from_bytes(lenght, 'little')          
        
        #Converte o tamanho da mensagem de network para host long (NtoHL)
        sockIntLen = socket.ntohl(sockLen)

        #Recebe a mensagem com o tamanho correto passado como parâmetro
        sString = self.socket.recv(sockIntLen)

        self.sexp = sexpr.str2sexpr(str(sString, 'utf-8'))


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
