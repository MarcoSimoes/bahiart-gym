import socket
import threading

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.connect(('localhost',3302))
# sock.setblocking(False)

msg = ''.encode()
def receive():
    while True:
        print(sock.recv(1024).decode())

def sendTo():
    while True:
        sock.sendall(input('> ').encode())

def start():
    threadRcvServer = threading.Thread(target=receive)
    threadSendServer = threading.Thread(target=sendTo)

    threadRcvServer.start()
    threadSendServer.start()

start()








# while True:
#     msg = input("> ")
#     if msg:
#     sock.sendall(msg.encode())

#     try:
#         msg = sock.recv(1024)
#         print(msg.decode('utf-8'))
#     except:
#         pass