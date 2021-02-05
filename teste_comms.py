import parser
import trainer
import comms
import world
#from connection import sParser, comand, Conection

ws = world.World()

while True:
    ws.net.updateSExp()
    ws.dynamicUpdate()

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