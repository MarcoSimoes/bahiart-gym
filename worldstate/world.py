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
        print("Tempo de Jogo: " + self.time)
        self.playMode = self.net.sParser.getValue('play_mode', self.net.sParser.parsedExp, self.playMode)
        print("PlayMode: " + self.playMode)
        self.scoreLeft = self.net.sParser.getValue('score_left', self.net.sParser.parsedExp, self.scoreLeft)
        print("score left: " + self.scoreLeft)
        self.scoreRight = self.net.sParser.getValue('score_right', self.net.sParser.parsedExp, self.scoreRight)
        print("score right: " + self.scoreRight)
    
    def staticUpdate(self):    

        #FIELD
        self.fieldLength = self.net.sParser.getValue('FieldLength', self.net.sParser.parsedExp)
        self.fieldHeight = self.net.sParser.getValue('FieldHeight', self.net.sParser.parsedExp)
        self.fieldwidth = self.net.sParser.getValue('FieldWidth', self.net.sParser.parsedExp)
        self.goalWidth = self.net.sParser.getValue('GoalWidth', self.net.sParser.parsedExp)
        self.goalDepth = self.net.sParser.getValue('GoalDepth', self.net.sParser.parsedExp)
        self.goalHeight = self.net.sParser.getValue('GoalHeight', self.net.sParser.parsedExp)

        #Mudança de lados não considerada!
        # self.theirGoalPos = Point(self.fieldLength, 0.0) #não consigo tratar o fieldlength direto na função de criação de ponto
        # self.ourGoalPos = Point(self.fieldLength, 0.0)

        #BALL
        self.ballRadius = self.net.sParser.getValue('BallRadius', self.net.sParser.parsedExp)
        self.ballMass = self.net.sParser.getValue('BallMass', self.net.sParser.parsedExp)
