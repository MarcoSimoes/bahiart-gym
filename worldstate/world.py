import socket
import parser
from server import trainer
from server.singleton import Singleton
from server import comms
from server import proxy
from geometry.geometry import Point

class World(Singleton):
    
    net = comms.Comms()
    proxy = proxy.Proxy()
    
    def __init__(self):
        self.time = None
        self.playMode = None
        self.scoreLeft = None
        self.scoreRight = None
    
    def dynamicUpdate(self):
        
        # while socket connected:
            #update dynamic variables

        #ENVIRONMENT
        self.time = self.net.sParser.getValue('time', self.net.sParser.parsedExp, self.time)
        self.playMode = self.net.sParser.getValue('play_mode', self.net.sParser.parsedExp, self.playMode)
        self.scoreLeft = self.net.sParser.getValue('score_left', self.net.sParser.parsedExp, self.scoreLeft)
        self.scoreRight = self.net.sParser.getValue('score_right', self.net.sParser.parsedExp, self.scoreRight)

        #DEBUG
        #print("Game Time: " + self.time)
        #print("score right: " + self.scoreRight)
        #print("score left: " + self.scoreLeft)
        #print("PlayMode: " + self.playMode)
    
    def staticUpdate(self):    

        #FIELD
        self.fieldLength = self.net.sParser.getValue('FieldLength', self.net.sParser.parsedExp)
        self.fieldHeight = self.net.sParser.getValue('FieldHeight', self.net.sParser.parsedExp)
        self.fieldwidth = self.net.sParser.getValue('FieldWidth', self.net.sParser.parsedExp)
        self.goalWidth = self.net.sParser.getValue('GoalWidth', self.net.sParser.parsedExp)
        self.goalDepth = self.net.sParser.getValue('GoalDepth', self.net.sParser.parsedExp)
        self.goalHeight = self.net.sParser.getValue('GoalHeight', self.net.sParser.parsedExp)

        #BALL
        self.ballRadius = self.net.sParser.getValue('BallRadius', self.net.sParser.parsedExp)
        self.ballMass = self.net.sParser.getValue('BallMass', self.net.sParser.parsedExp)
