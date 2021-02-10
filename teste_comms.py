import parser
import trainer
from server import comms
from server import proxy
from worldstate import world
#from connection import sParser, comand, Conection

ws = world.World()
proxy = proxy.Proxy()

proxy.run()

# while True:    
#     ws.net.updateSExp()
#     ws.dynamicUpdate()
# test = net.sParser.getValue('GoalDepth', net.sParser.parsedExp)
# ws.staticUpdate()
# print(net.sParser.parsedExp)

# while True:
#     net.updateSExp()
#     time = net.sParser.getValue('time', net.sParser.parsedExp)
#     print(time)
#     if time != None:
#         print(time)