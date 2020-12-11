import subprocess as proc
import socket
import sys
import sexpr
import parser


#proc.run(["rcssserver3d", "&"])        #Melhor iniciar numa janela do terminal mesmo por hora
HOST = 'localhost'
PORT = 3200
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))


lenght = sock.recv(4)                               #Recebe os primeiros 4 bytes que dizem respeito ao tamanho da mensagem                                
sockLen = int.from_bytes(lenght, 'little')          #Converte os bytes da mensagem em inteiro, com os bytes ordenados do menor para o maior (little)
sockIntLen = socket.ntohl(sockLen)                  #Converte o tamanho da mensagem de network para host long (NtoHL)

sString = sock.recv(sockIntLen)                     #Recebe a mensagem com o tamanho correto passado como parâmetro

sexp = sexpr.str2sexpr(str(sString, 'utf-8'))

parser.search('play_mode', sexp)

# serverMsgFile = open("serverExpression.txt", "w")
# serverMsgFile.write(str(sexp))
# serverMsgFile.close()