import socket
from agentProxy import agentProxy

class Proxy:


    def __init__(self,agent_port,server_port=3100,server_host='localhost'):

        self.SERVER_HOST = server_host
        self.SERVER_PORT = server_port
        self.AGENT_PORT = agent_port

        self.agentSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.agentSock.bind((self.SERVER_HOST, self.AGENT_PORT))

        self.proxies = []

    def start(self):
        while True:
            self.agentSock.listen()
            newAgentSock, _ = self.agentSock.accept()

            try:
                pxy = agentProxy(newAgentSock,self.SERVER_PORT,self.SERVER_HOST)
                pxy.connectionManager()
                self.proxies.append(pxy)
                print("[PROXY] New agent connected on port : " + str(self.AGENT_PORT))
            except:
                print("[PROXY] Couldn't connect new agent.")