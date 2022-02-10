import sys
sys.path.append("../")
import gym
import numpy as np
from gym import spaces
from server.player import Player
from server.trainer import Trainer
from server.world import World
from gym_rcssserver3d.agentcomms import AgentComms
from gym_rcssserver3d.agentcomms import InvalidHostAndPortLengths

import numpy as np

sys.path.append("../../server")

from server import *

class DemoEnv(gym.Env):
    metadata = {'render.modes': ['human']}

    optPlayer: Player = None

    def __init__(self):
        
        #CREATING WORLD OBJECT AND UPDATING ITS VARIABLES
        self.agents=AgentComms()   
        self.command = Trainer()
        self.ws = World()
        self.ws.staticUpdate()
        self.ws.dynamicUpdate()

        self.episodeInitTime = None
        self.episodeInitBallPos = None
        self.reward = 100
        self.goalsScored = 0
        
        self.action_space = spaces.Discrete(3)
        self.observation_space = spaces.Box(np.array([0, 0]), np.array([60, 300])) #BallDist goes from 0 to 60. BallSpeed goes from 0 to 300.

        self.state = np.array([0.0,0.0])

        self.thisStep = 0

    def step(self, action): 
        """
            Takes an action, whether to stand still, walk towards the ball or kick the ball.
        """

        self.command.reqFullState()
        self.ws.staticUpdate()
        self.ws.dynamicUpdate()

        if(self.episodeInitTime is None):
            self.episodeInitTime = self.ws.time
        if(self.episodeInitBallPos is None):
            self.episodeInitBallPos = np.array([self.ws.ballFinalPos[0], self.ws.ballFinalPos[1]])

        message = str(action)            
        self.agents.sendAll(message)
        self.agents.receiveAll()

        self.ws.dynamicUpdate()
        
        obsBallDist = self.optPlayer.ballPolarPos[0]
        obsBallSpeed = self.ws.ballSpeed
        self.state = np.array([obsBallDist, obsBallSpeed])
        
        #Verify if episode is done either by scoring a goal or having passed 1 minute since the start of the episode.
        if(self.goalsScored < self.ws.scoreLeft or (self.ws.time - self.episodeInitTime) > 20):
            done = True
            currTime = self.ws.time
            elapsedTime = currTime - self.episodeInitTime
            episodeEndBallPos = np.array([self.ws.ballFinalPos[0], self.ws.ballFinalPos[1]])
            ballTravDist = np.linalg.norm(episodeEndBallPos - self.episodeInitBallPos)
            if(ballTravDist < 5.0):
                reward = ballTravDist
            elif(ballTravDist < 10):
                reward = ballTravDist*3
            elif(ballTravDist < 20):
                reward = ballTravDist*5
            self.episodeInitTime = None
            self.episodeInitBallPos = None
            if(self.goalsScored < self.ws.scoreLeft):
                self.goalsScored += 1
                reward = reward*10
            print("Elapsed Time: {} / BallTravDist: {} / Reward: {}".format(elapsedTime, ballTravDist, reward))
        else:
            reward = 0
            done = False

        info = {}

        return self.state, reward, done, info

    def reset(self):
        '''
            Resets player and ball to default positions.
            WARNING: GUARANTEE THE PLAYER IS STANDING UP BEFORE RESETING
        '''
        self.ws.staticUpdate()
        self.ws.dynamicUpdate()
        if(self.ws.playMode == 13):
            self.command.changePlayMode("PlayOn") # if playmode is GoalLeft, sets playmode to playOn
        
        #Place the ball in the center of the field
        self.command.beamBall(-3.0, 0.0, 0.0)

        #Place the Player behind the ball
        self.command.beamPlayer(self.optPlayer.getUnum(), "Left", -5.0, 0, 0.3)

        obsBallDist = self.optPlayer.ballPolarPos[0]
        obsBallSpeed = self.ws.ballSpeed
        self.state = np.array([obsBallDist, obsBallSpeed])

        return self.state

    def render(self, mode='human'): # Run roboviz or any monitor in the screen to show the training
        ...
  
    def setPlayer(self, player: Player):
        self.optPlayer = player

    def stayIdleBeforeKickOff(self):
        while True:
            self.ws.dynamicUpdate()
            if(self.ws.playMode != 0):
                break

    def close(self):
        ...
