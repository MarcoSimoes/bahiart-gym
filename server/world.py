from server.comms import Comms
from server.singleton import Singleton

class World(Singleton):
    
    net = Comms()
    parser = net.serverParser
    
    def __init__(self):
        
        #DYNAMIC
        self.time = None
        self.playMode = None
        self.scoreLeft = None
        self.scoreRight = None

        #STATIC
        self.fieldLength = None
        self.fieldHeight = None
        self.fieldwidth = None
        self.goalWidth = None
        self.goalDepth = None
        self.goalHeight = None

        #BALL
        self.ballRadius = None
        self.ballMass = None
        self.ballPos = None
        self.ballNode = None
        self.ballGraph = None

    
    def dynamicUpdate(self):
        
        # while socket connected:
            #update dynamic variables
        self.net.updateSExp()
        serverExp = self.net.serverExp

        #ENVIRONMENT
        self.time = float(self.parser.getValue('time', serverExp, self.time))
        self.playMode = int(self.parser.getValue('play_mode', serverExp, self.playMode))
        self.scoreLeft = int(self.parser.getValue('score_left', serverExp, self.scoreLeft))
        self.scoreRight = int(self.parser.getValue('score_right', serverExp, self.scoreRight))

        #BALLPOS
        self.ballNode = self.parser.setBallNd(serverExp)
        self.ballGraph = self.parser.getBallGraph(self.ballNode, self.ballGraph)
        self.ballPos = self.parser.getBallPos(self.ballGraph, self.ballPos)


        #DEBUG
        #print("Game Time: " + self.time)
        #print("score right: " + self.scoreRight)
        #print("score left: " + self.scoreLeft)
        #print("PlayMode: " + self.playMode)
    
    def staticUpdate(self):    
        self.net.updateSExp()
        serverExp = self.net.serverExp

        #FIELD
        self.fieldLength = float(self.parser.getValue('FieldLength', serverExp, self.fieldLength))
        self.fieldHeight = float(self.parser.getValue('FieldHeight', serverExp, self.fieldHeight))
        self.fieldwidth = float(self.parser.getValue('FieldWidth', serverExp, self.fieldwidth))
        self.goalWidth = float(self.parser.getValue('GoalWidth', serverExp, self.goalWidth))
        self.goalDepth = float(self.parser.getValue('GoalDepth', serverExp, self.goalDepth))
        self.goalHeight = float(self.parser.getValue('GoalHeight', serverExp, self.goalHeight))

        #BALL
        self.ballRadius = float(self.parser.getValue('BallRadius', serverExp, self.ballRadius))
        self.ballMass = float(self.parser.getValue('BallMass', serverExp, self.ballMass))
