#from server.trainer import Trainer
from server.world import World

ws = World()

while True:
    #ws.net.updateSExp()
    ws.dynamicUpdate()
    print(ws.ballPos)
    #print("time: " + str(ws.time))
    #print("playMode: " + str(ws.playMode))
    #print(ws.net.serverExp)
    print("\n")

# command = Trainer()

# #command.changePlayMode("PlayOn")
# command.beamBall(0,0,0)
# command.beamPlayer(1, "Left", -0.15, 0, 0.3)