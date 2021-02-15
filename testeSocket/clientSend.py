import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 32123))
while True:
    msg = input("> ")
    s.sendall(msg.encode())
    # data = s.recv(1024)
    # print ('Received : ' + repr(data))
s.close()
