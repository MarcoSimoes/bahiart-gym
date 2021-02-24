# from proxy import Proxy

# prox = Proxy()
# prox.start_serverSock()
# prox.start_agentSock()
# while 1:
#     prox.receiveAgentMessage()
#     print('Recv Agent')
#     prox.forwardAgentMessage()
#     print('Sent Agent -> Server')
#     prox.receiveServerMessage()
#     print('Receive Server')
#     prox.forwardServerMessage()
#     print('Sent Server -> Agent')

import socket
import threading

serverHOST = 'localhost'

# CONNECTING TO AGENT

agentPORT = 3300

agentProxyAddress = (serverHOST, agentPORT)
agentSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
agentSock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
agentSock.bind(agentProxyAddress)
agentSock.listen()
print('Waiting agent to connect on port : ' + str(agentPORT))
agentConnection, _ = agentSock.accept()
print('Agent connected')




# CONNECTING TO SERVER


serverPORT = 3100

serverSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSock.connect((serverHOST, serverPORT))
# serverSock.setblocking(False)
print("Connected to server on port : " + str(serverPORT))


        

agentMessage = ''.encode()
serverMessage = ''.encode()     

def receivingFromAgent():
    while True:
        agentMessage = agentConnection.recv(4)
        print('Receive from agent')
        
def receivingFromServer():
    while True:
        serverMessage = serverSock.recv(4)
        print('Receive from server')            

def sendToServer():
    while True:
        serverSock.sendall(agentMessage)
        print('Send to server')

def sendToAgent():
    while True:
        agentConnection.sendall(serverMessage)
        print('Send to agent')

def start():
    threadRcvAgent = threading.Thread(target=receivingFromAgent)
    threadRcvServer = threading.Thread(target=receivingFromServer)
    threadSendServer = threading.Thread(target=sendToServer) 
    threadSendAgent = threading.Thread(target=sendToAgent)

    threadRcvAgent.start()
    threadSendAgent.start()
    threadRcvServer.start()
    threadSendServer.start()

start()

# while True:
#     msg = agentConnection.recv(1024)
#     print("Rcv Ag")
#     serverSock.sendall(msg)
#     print("Sent to Server")

#     msg = serverSock.recv(1024)
#     print("Rcv Server")
#     agentConnection.sendall(msg)
#     print("Sent Agt")

