from proxy import Proxy
from agentParser import AgentParser
import sys

# TO RUN TYPE : python3 runProxy.py <agentConnectionPort>
# Ex: python3 runProxy.py 3300
#proxy = Proxy(int(sys.argv[1]))
proxy = Proxy(3500)

#  -------------------- OPTION 1 ------------------------
# TO RUN THE PROXY
proxy.start()

#Intance Parser
parser = AgentParser()
GYRVal = None
while True:
    lista = proxy.getMessagesFromAgent('1')
    parsedExp = parser.parse(str(lista))
    GYRVal = parser.getGyr('GYR', parsedExp, GYRVal)
    if len(lista) == 0:
        pass
    else:
        print(GYRVal)
        #print(lista)


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
