""" import socket
import parser
import trainer
from connection import sParser

class World:
    
    def __init__(self, sock: socket):


        #FIELD
        self.fieldLength = sParser.getValue('FieldLength', sParser.sexp)
        self.fieldHeight = sParser.getValue('FieldHeight', sParser.sexp)
        self.fieldwidth = sParser.getValue('Fieldwidth', sParser.sexp)
        self.goalWidth = sParser.getValue('GoalWidth', sParser.sexp)
        self.goalDepth = sParser.getValue('GoalDepth', sParser.sexp)
        self.goalHeight = sParser.getValue('GoalHeight', sParser.sexp)

        #BALL
        self.ballRadius = sParser.getValue('BallRadius', sParser.sexp)
        self.ballMass = sParser.getValue('BallMass', sParser.sexp)

    def updateEnv(self):
        
        #ENVIRONMENT
        self.time = sParser.getValue('time', sParser.sexp)
        self.playMode = sParser.getValue('play_mode', sParser.sexp)
        self.scoreLeft = sParser.getValue('score_left', sParser.sexp)
        self.scoreRight = sParser.getValue('score_right', sParser.sexp)

    pass """