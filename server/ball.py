import sys
import numpy as np
from server.singleton import Singleton

class Ball(Singleton):

    def __init__(self):
        super().__init__()
        self.latestServerPos = None
        self.currentServerPos = None

    def updateServer(self, ballPos, time):
        if(not self.latestServerPos):
            self.latestServerPos = ballPos
            self.currentServerPos = ballPos
            self.latestServerTime = time
            self.currentServerTime = time

            self.speedBallServer = 0.0
        else:
            self.latestServerPos = self.currentServerPos
            self.currentServerPos = ballPos
            self.latestServerTime = self.currentServerTime
            self.currentServerTime = time

            a = np.array((self.latestServerPos[0], self.latestServerPos[1], self.latestServerPos[2]))
            b = np.array((self.currentServerPos[0], self.currentServerPos[1], self.currentServerPos[2]))

            dist = np.linalg.norm(b-a)
                
            self.speedBallServer = dist / (self.currentServerTime - self.latestServerTime)        

    def updatePlayer(self, ballPos, time):
        self.speedBallPlayer
        pass