import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('localhost', 32123))
s.listen(1)
conn, addr = s.accept()
while 1:
    data = conn.recv(1024)
    print('Received : ' ,repr(data.decode()))
    # msg = input('> ')
    # s.sendall(msg.encode())
    
conn.close()