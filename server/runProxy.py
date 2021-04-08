from proxy import Proxy
import sys

# TO RUN TYPE : python3 runProxy.py <agentConnectionPort>
# Ex: python3 runProxy.py 3300
proxy = Proxy(int(sys.argv[1]))
proxy.start()
