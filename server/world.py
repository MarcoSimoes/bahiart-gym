from server.comms import Comms
from server.ball import Ball
from server.singleton import Singleton

class World(Singleton):
    
    net = Comms()
    ball = Ball()
    parser = net.serverParser
    
    def __init__(self):
        
        #DYNAMIC
        self.time = 0.0
        self.playMode = 0
        self.scoreLeft = 0
        self.scoreRight = 0

        #STATIC
        self.fieldLength = 0.0
        self.fieldHeight = 0.0
        self.fieldwidth = 0.0
        self.goalWidth = 0.0
        self.goalDepth = 0.0
        self.goalHeight = 0.0

        #BALL
        self.ballRadius = 0.0
        self.ballMass = 0.0
        self.ballPos = None
        self.ballNode = None
        self.ballGraph = None

    
    def dynamicUpdate(self):
        
        serverExp = []
        try:
            self.net.updateSExp()
            serverExp = self.net.serverExp
        except Exception as e:
            #pass
            print("-----SERVER S-EXPRESSION UPDATE ERROR-----:")
            print(e)
        #print(serverExp)
        # except:
        #     print("Skipped server EXP update --------------------------------------")
        
        #ENVIRONMENT
        try:
            self.time = float(self.parser.getValue('time', serverExp, self.time))
            self.playMode = int(self.parser.getValue('play_mode', serverExp, self.playMode))
            self.scoreLeft = int(self.parser.getValue('score_left', serverExp, self.scoreLeft))
            self.scoreRight = int(self.parser.getValue('score_right', serverExp, self.scoreRight))
        except Exception as e:
            pass
            #print("-----ENVIRONMENT EXCEPTION-----: ")
            #print(e)

        #BALLPOS
        try:
            self.ballNode = self.parser.setBallNd(serverExp)
            self.ballGraph = self.parser.getBallGraph(self.ballNode, self.ballGraph)
            self.ballPos = self.parser.getBallPos(self.ballGraph, self.ballPos)

            if(self.ballPos is not None):
                self.ball.updateServer(self.ballPos, self.time)
            else:
                pass
                #DEBUG
                #print("BALL POS IS NONE")
        except Exception as e:
            pass
            #print("-----BALLPOSS EXCEPTION-----:")
            #print(e)

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
