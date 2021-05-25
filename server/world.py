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
        self.time = self.parser.getValue('time', serverExp, self.time)
        self.playMode = self.parser.getValue('play_mode', serverExp, self.playMode)
        self.scoreLeft = self.parser.getValue('score_left', serverExp, self.scoreLeft)
        self.scoreRight = self.parser.getValue('score_right', serverExp, self.scoreRight)

        #BALLPOS
        self.ballNode = self.parser.setBallNd(serverExp)
        self.ballGraph = self.parser.getBallGraph(self.ballNode, self.ballGraph)
        
        #NOT WORKING YET
        #self.ballPos = self.parser.getBallPos(self.ballGraph)


        #DEBUG
        #print("Game Time: " + self.time)
        #print("score right: " + self.scoreRight)
        #print("score left: " + self.scoreLeft)
        #print("PlayMode: " + self.playMode)
    
    def staticUpdate(self):    
        self.net.updateSExp()
        serverExp = self.net.serverExp

        #FIELD
        self.fieldLength = self.parser.getValue('FieldLength', serverExp, self.fieldLength)
        self.fieldHeight = self.parser.getValue('FieldHeight', serverExp, self.fieldHeight)
        self.fieldwidth = self.parser.getValue('FieldWidth', serverExp, self.fieldwidth)
        self.goalWidth = self.parser.getValue('GoalWidth', serverExp, self.goalWidth)
        self.goalDepth = self.parser.getValue('GoalDepth', serverExp, self.goalDepth)
        self.goalHeight = self.parser.getValue('GoalHeight', serverExp, self.goalHeight)

        #BALL
        self.ballRadius = self.parser.getValue('BallRadius', serverExp, self.ballRadius)
        self.ballMass = self.parser.getValue('BallMass', serverExp, self.ballMass)
