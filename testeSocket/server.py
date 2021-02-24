import socket
import threading

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind(("localhost",3301))
sock.listen(1)
connectionClient, _ = sock.accept()


def receive():
    while True:         
        print(str(connectionClient.recv(1024).decode()))

def sendTo():
    while True:
        msgtos = input('> ')
        connectionClient.sendall(msgtos.encode())


threadRcvAgent = threading.Thread(target=receive)
threadSendAgent = threading.Thread(target=sendTo)

threadRcvAgent.start()
threadSendAgent.start()

# while True:
    

#     try:
#         msg = connectionClient.recv(1024)
#         print(str(msg.decode()))
#     except:
#         pass
#     msg = input("> ")
#     if msg:
#         sock.sendall(msg.encode('utf-8'))
    