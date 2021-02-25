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
serverPORT = 3300
agentPORT = 3400
FORMAT = 'utf-8'



# CONNECTING TO AGENT

agentProxyAddress = (serverHOST, agentPORT)
agentSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
agentSock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
agentSock.bind(agentProxyAddress)
agentSock.listen()
print('Waiting agent to connect on port : ' + str(agentPORT))
agentConnection, _ = agentSock.accept()
print('Agent connected')


# CONNECTING TO SERVER

serverSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSock.connect((serverHOST, serverPORT))
# serverSock.setblocking(False)
print("Connected to server on port : " + str(serverPORT))


# FUNCTIONS

agentMessage = 'ELE ESTÁ ENVIANDO ESSA MENSAGEM SEM ATUALIZAR'.encode()
serverMessage = 'ELE ESTÁ ENVIANDO ESSA MENSAGEM SEM ATUALIZAR'.encode()

def sendToServer():
    # while True:
    try:
        print('[AGENT -> SERVER]' + agentMessage.decode())
    except:
        print('[AGENT -> SERVER]couldn\'t decode' )
    serverSock.sendall(agentMessage)
    # print('[AGENT]' + str(agentMessage.decode(FORMAT)))

def sendToAgent():
    # while True:
    try:
        print('[SERVER -> AGENT]' + serverMessage.decode())
    except:
        print('[SERVER -> AGENT]couldn\'t decode' )
    agentConnection.sendall(serverMessage)
    # print('[SERVER]' + str(serverMessage.decode(FORMAT)))

def receivingFromAgent():
    global agentMessage
    while True:
        agentMessage = agentConnection.recv(1024)
        try:
            print('[AGENT]' + str(agentMessage.decode()))
        except:
            print('[AGENT]couldn\'t decode')
        threadSendServer = threading.Thread(target=sendToServer)
        threadSendServer.start()
        
def receivingFromServer():
    global serverMessage
    while True:
        serverMessage = serverSock.recv(1024)
        try:
            print('[SERVER]' + str(serverMessage.decode())) 
        except:
            print('[SERVER]couldn\'t decode')
        threadSendAgent = threading.Thread(target=sendToAgent)
        threadSendAgent.start()
           



def start():
    threadRcvAgent = threading.Thread(target=receivingFromAgent)
    threadRcvServer = threading.Thread(target=receivingFromServer)
    # threadSendServer = threading.Thread(target=sendToServer) 
    # threadSendAgent = threading.Thread(target=sendToAgent)

    threadRcvAgent.start()
    # threadSendAgent.start()
    threadRcvServer.start()
    # threadSendServer.start()

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



















# 
# Waiting agent to connect on port : 3400
# Agent connected
# Connected to server on port : 3300
# [AGENT]+(scene rsg/agent/nao/nao_hetero.rsg 4)(syn)
# [AGENT -> SERVER]+(scene rsg/agent/nao/nao_hetero.rsg 4)(syn)
# Exception in thread Thread-2:
# Traceback (most recent call last):
#   File "/usr/lib/python3.6/threading.py", line 916, in _bootstrap_inner
    # self.run()
#   File "/usr/lib/python3.6/threading.py", line 864, in run
    # self._target(*self._args, **self._kwargs)
#   File "proxyTeste.py", line 75, in receivingFromServer
    # print('[SERVER]' + str(serverMessage.decode()))
# UnicodeDecodeError: 'utf-8' codec can't decode byte 0xeb in position 3: invalid continuation byte
# 
# ^CException ignored in: <module 'threading' from '/usr/lib/python3.6/threading.py'>
# Traceback (most recent call last):
#   File "/usr/lib/python3.6/threading.py", line 1294, in _shutdown
    # t.join()
#   File "/usr/lib/python3.6/threading.py", line 1056, in join
    # self._wait_for_tstate_lock()
#   File "/usr/lib/python3.6/threading.py", line 1072, in _wait_for_tstate_lock
    # elif lock.acquire(block, timeout):
# KeyboardInterrupt
# 