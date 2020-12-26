import parser
import trainer
import comms
import world
#from connection import sParser, comand, Conection

net = comms.Comms()
#ws = world.World()
# while True:    
#     net.updateSExp()
#     ws.dynamicUpdate()
#     print(ws.time)

while True:
    net.updateSExp()
    tempo = net.sParser.getValue('time', net.sParser.parsedExp)
    print(tempo)
    # if tempo != None:
    #     print(tempo)