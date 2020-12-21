import socket
import parser
import trainer
from comms import sParser

class World(object):
    
    _instance = None

    time = None
    playMode = None
    scoreLeft = None
    scoreRight = None

    def __new__(self):
        if not self._instance:
            self._instance = super(World, self).__new__(self)
            
        return self._instance
    
    def updateEnv(self):
        
        #ENVIRONMENT
        self.time = sParser.getValue('time', sParser.sexp)
        self.playMode = sParser.getValue('play_mode', sParser.sexp)
        self.scoreLeft = sParser.getValue('score_left', sParser.sexp)
        self.scoreRight = sParser.getValue('score_right', sParser.sexp)

    #FIELD
    fieldLength = sParser.getValue('FieldLength', sParser.sexp)
    fieldHeight = sParser.getValue('FieldHeight', sParser.sexp)
    fieldwidth = sParser.getValue('Fieldwidth', sParser.sexp)
    goalWidth = sParser.getValue('GoalWidth', sParser.sexp)
    goalDepth = sParser.getValue('GoalDepth', sParser.sexp)
    goalHeight = sParser.getValue('GoalHeight', sParser.sexp)

    #BALL
    ballRadius = sParser.getValue('BallRadius', sParser.sexp)
    ballMass = sParser.getValue('BallMass', sParser.sexp)
