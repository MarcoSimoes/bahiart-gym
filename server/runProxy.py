from proxy import Proxy
import sys

# TO RUN TYPE : python3 runProxy.py <agentConnectionPort>
# Ex: python3 runProxy.py 3300
proxy = Proxy(int(sys.argv[1]))


#  -------------------- OPTION 1 ------------------------
# TO RUN THE PROXY
proxy.start()

while True:
    lista = proxy.getMessagesFromAgent('1')
    if len(lista) == 0:
        pass
    else:
        print(lista)


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
