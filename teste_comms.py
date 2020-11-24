import subprocess as proc
import socket
import sys
from sexpdata import loads, dumps


#proc.run(["rcssserver3d", "&"])        #Melhor iniciar numa janela do terminal mesmo por hora
HOST = 'localhost'
PORT = 3200
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))

#msg = "(playMode kickOff_Left)"         #Constroi a mensagem
#msgLen = socket.htonl(len(msg))         #pega o tamanho da mensagem e traduz utilizando o metodo Host To Network Long
#prefix = msgLen.to_bytes(4, 'little')   #converte o tamanho de inteiro para bytes no formato little, assim como é devolvido pelo servidor.

#fullmsg = str(prefix, "utf-8") + msg    #concatena o prefixo com a mensagem, transformando o prefixo em string com encode em utf-8, evitando duplicação do "b" de mensagens em bytes

#sock.send(fullmsg.encode())             #encoda a mensagem e envia ela pelo socket TCP

data = sock.recv(1024*10)
#hexbytes = data[0:4]
#hexInt = int.from_bytes(hexbytes, byteorder='big', signed=False)      #traduz o inicio da mensagem de bytes para inteiro
#print(data)

#msgCodada = fullmsg.encode()

#print("Mensagem codada: " + str(msgCodada))


# while True:
#     data = sock.recv(4523)
#     data = repr(data)
#     print(data)

data2 = repr(data)
#print(data2)
loads(data2)
print(dumps(['FieldLenght']))

#decodedData = data[4:].decode()
# serverMsgFile = open("mensagemDoServer.txt", "w")
# serverMsgFile.write(decodedData)
# serverMsgFile.close()
# print("pronto")




