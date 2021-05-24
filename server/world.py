from server.comms import Comms
from server.singleton import Singleton

class World(Singleton):
    
    net = Comms()
    
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

    
    def dynamicUpdate(self):
        
        # while socket connected:
            #update dynamic variables
        serverExp = self.net.serverExp

        #ENVIRONMENT
        self.time = self.net.sParser.getValue('time', serverExp, self.time)
        self.playMode = self.net.sParser.getValue('play_mode', serverExp, self.playMode)
        self.scoreLeft = self.net.sParser.getValue('score_left', serverExp, self.scoreLeft)
        self.scoreRight = self.net.sParser.getValue('score_right', serverExp, self.scoreRight)

        #DEBUG
        #print("Game Time: " + self.time)
        #print("score right: " + self.scoreRight)
        #print("score left: " + self.scoreLeft)
        #print("PlayMode: " + self.playMode)
    
    def staticUpdate(self):    

        serverExp = self.net.serverExp

        #FIELD
        self.fieldLength = self.net.sParser.getValue('FieldLength', serverExp, self.fieldLength)
        self.fieldHeight = self.net.sParser.getValue('FieldHeight', serverExp, self.fieldHeight)
        self.fieldwidth = self.net.sParser.getValue('FieldWidth', serverExp, self.fieldwidth)
        self.goalWidth = self.net.sParser.getValue('GoalWidth', serverExp, self.goalWidth)
        self.goalDepth = self.net.sParser.getValue('GoalDepth', serverExp, self.goalDepth)
        self.goalHeight = self.net.sParser.getValue('GoalHeight', serverExp, self.goalHeight)

        #BALL
        self.ballRadius = self.net.sParser.getValue('BallRadius', serverExp, self.ballRadius)
        self.ballMass = self.net.sParser.getValue('BallMass', serverExp, self.ballMass)
