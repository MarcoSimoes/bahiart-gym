import sys
# sys.path.append('/home/mask/workspace/bahiart-openaigym')

from server.proxy import Proxy
from server.agentParser import AgentParser


# TO RUN TYPE : python3 runProxy.py <agentConnectionPort>
# Ex: python3 runProxy.py 3300
#proxy = Proxy(int(sys.argv[1]))
proxy = Proxy(3500)

#  -------------------- OPTION 1 ------------------------
# TO RUN THE PROXY
proxy.start()

#Intance Parser
parser = AgentParser()
agent = None
while True:
    #lista = proxy.getMessagesFromAgent('1')
    if agent == None:
        agent = proxy.getPlayerObj('1')
    else:
        if agent.getUnum() == None:
            pass
        else:
            pass
            print(agent.neckYaw)

#  -------------------- OPTION 2 ------------------------
# TO RUN THE PROXY IN ANOTHER THREAD AND STILL BE ABLE TO CALL 
# ANOTHER FUNCTIONS WITHOUT BEING STUCK IN THE START FUNCTION.

# IN THIS WAY, WE CAN RECEIVE THE MESSAGES FROM A SPECIFIC AGENT
# proxy.main()

# while True:
#    msg = proxy.getMessagesFromAgent('1')
#    if msg != '':
#        print(msg)
#        print("\n")
