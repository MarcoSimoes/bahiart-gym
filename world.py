import socket
import parser
import trainer
import comms

class World(object):
    
    net = comms.Comms()
    _instance = None

    def __new__(self):
        if not self._instance:
            self._instance = super(World, self).__new__(self)
            
        return self._instance
    
    def dynamicUpdate(self):
        
        # while socket connected:
            #update dynamic variables

        #ENVIRONMENT
        self.time = self.net.sParser.getValue('time', self.net.sParser.parsedExp)
        self.playMode = self.net.sParser.getValue('play_mode', self.net.sParser.parsedExp)
        self.scoreLeft = self.net.sParser.getValue('score_left', self.net.sParser.parsedExp)
        self.scoreRight = self.net.sParser.getValue('score_right', self.net.sParser.parsedExp)

    def staticUpdate(self):    

        #FIELD
        self.fieldLength = self.net.sParser.getValue('FieldLength', self.net.sParser.parsedExp)
        self.fieldHeight = self.net.sParser.getValue('FieldHeight', self.net.sParser.parsedExp)
        self.fieldwidth = self.net.sParser.getValue('Fieldwidth', self.net.sParser.parsedExp)
        self.goalWidth = self.net.sParser.getValue('GoalWidth', self.net.sParser.parsedExp)
        self.goalDepth = self.net.sParser.getValue('GoalDepth', self.net.sParser.parsedExp)
        self.goalHeight = self.net.sParser.getValue('GoalHeight', self.net.sParser.parsedExp)

        #BALL
        self.ballRadius = self.net.sParser.getValue('BallRadius', self.net.sParser.parsedExp)
        self.ballMass = self.net.sParser.getValue('BallMass', self.net.sParser.parsedExp)
