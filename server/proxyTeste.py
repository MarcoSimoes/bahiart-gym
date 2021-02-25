from proxy import Proxy

prox = Proxy()
prox.start_serverSock()
prox.start_agentSock()
while 1:
    prox.receiveAgentMessage()
    prox.forwardAgentMessage()