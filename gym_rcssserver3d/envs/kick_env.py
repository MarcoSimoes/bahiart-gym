import sys
sys.path.append("../")
import gym
from gym import spaces
from server.player import Player
from server.trainer import Trainer
from server.world import World
from gym_rcssserver3d.agentcomms import AgentComms
from gym_rcssserver3d.agentcomms import InvalidHostAndPortLengths

import numpy as np

sys.path.append("../../server")


from server import *

class KickEnv(gym.Env):
    metadata = {'render.modes': ['human']}

    optPlayer: Player = None

    def __init__(self):
        
#        input()  
        self.agents=AgentComms()   
#        input()                    
        #CREATING WORLD OBJECT AND UPDATING ITS VARIABLES
        self.command = Trainer()
        self.ws = World()
        self.ws.staticUpdate()
        self.ws.dynamicUpdate()

        self.episodeInitTime = None
        self.initBallPos = None
        
        self.createActionSpace()
        self.createObservationSpace()

        self.thisStep = 0
        self.prevAction = None

        #Define episode end condition flags
        self.episodeTimeLimit = 5.0
        self.endEpisodeIfFallen = True

    def step(self, action, thisStep): 
        """
            Actions based in numbers passed to the joints. 
            22 joints total (define which one will be used in each train)
        """

    
        self.command.reqFullState()
        self.ws.staticUpdate()
        self.ws.dynamicUpdate()
        self.prevAction = action
        self.thisStep = thisStep

        if(self.episodeInitTime is None):
            self.episodeInitTime = self.ws.time
        if(self.initBallPos is None):
            self.initBallPos = self.ws.ballFinalPos[0]
        reward = 0

        # 1 - Organize actions in a list to be sent to the team.
        myList = []

        for i in range(0, len(action)):
            for j in range(0, len(action[i])):
                myList.append(action[i,j])

        message=""

        for value in myList:
            message+=(str(value))
            message+=','
            
        self.agents.sendAll(message)
        
        self.agents.receiveAll()

        self.ws.dynamicUpdate()
        currBallPos = self.ws.ballFinalPos[0]
        currTime = self.ws.time
        elapsedTime = currTime - self.episodeInitTime
        self.state = self.optPlayer.getObs()
        self.state['prevAction'] = self.prevAction
        self.state['count'] = self.thisStep
        
        #Verify if episode is done
        if((elapsedTime > self.episodeTimeLimit) or (self.endEpisodeIfFallen and self.optPlayer.checkFallen())):
            done = True
            self.initBallPos = None
            self.episodeInitTime = None
        else:
            done = False
        

        info = {}
        reward = 0 #There is no reward on this default environment

        return self.state, reward, done, info

    def reset(self):

        self.ws.staticUpdate()
        self.ws.dynamicUpdate()
        
        #Place the ball in the center of the field
        self.command.beamBall(0.0, 0.0, 0.0)

        #Place the Player behind the ball
        self.command.beamPlayer(self.optPlayer.getUnum(), "Left", -0.2, 0, 0.3)

        self.state = self.optPlayer.getObs()
        self.state['prevAction'] = self.prevAction
        self.state['count'] = self.thisStep

        return self.state

    def render(self, mode='human'): # Run roboviz or any monitor in the screen to show the training
        ...
  
    def setPlayer(self, player: Player):
        self.optPlayer = player

    def createActionSpace(self):
        self.action_space = spaces.Box(
            np.array([
                [-120.0, -6.109],     #hj1 (angle, angular vel) MIN
                [-45.0, -6.109],      #hj2
                [-90.0, -6.109],      #llj1
                [-120.0, -6.109],     #rlj1
                [-25.0, -6.109],      #llj2
                [-45.0, -6.109],      #rlj2
                [-25.0, -6.109],      #llj3
                [-25.0, -6.109],      #rlj3
                [-130.0, -6.109],     #llj4
                [-130.0, -6.109],     #rlj4
                [-45.0, -6.109],      #llj5
                [-45.0, -6.109],      #rlj5
                [-45.0, -6.109],      #llj6
                [-25.0, -6.109],      #rlj6
                [-120.0, -6.109],     #laj1
                [-120.0, -6.109],     #raj1
                [-1.0, -6.109],       #laj2
                [-95.0, -6.109],      #raj2
                [-120.0, -6.109],     #laj3
                [-120.0, -6.109],     #raj3
                [-90.0, -6.109],      #laj4
                [-1.0, -6.109]]),     #raj4
            np.array([
                [120.0, 6.109],      #hj1 (angle, angular vel) MAX
                [45.0, 6.109],       #hj2
                [1.0, 6.109],        #llj1
                [120.0, 6.109],      #rlj1
                [45.0, 6.109],       #llj2
                [25.0, 6.109],       #rlj2
                [100.0, 6.109],      #llj3
                [100.0, 6.109],      #rlj3
                [1.0, 6.109],        #llj4
                [1.0, 6.109],        #rlj4
                [75.0, 6.109],       #llj5 
                [75.0, 6.109],       #rlj5
                [25.0, 6.109],       #llj6
                [45.0, 6.109],       #rlj6
                [120.0, 6.109],      #laj1
                [120.0, 6.109],      #raj1
                [95.0, 6.109],       #laj2
                [1.0, 6.109],        #raj2
                [120.0, 6.109],      #laj3
                [120.0, 6.109],      #raj3
                [1.0, 6.109],        #laj4
                [90.0, 6.109]]),     #raj4
                dtype=np.float64)

    def createObservationSpace(self):
    
        self.observation_space = spaces.Dict({
        'joints': spaces.Dict({
            'neckYaw': spaces.Box(low=np.array([-120]), high=np.array([120]), dtype=np.float64),
            'neckPitch': spaces.Box(low=np.array([-45]), high=np.array([45]), dtype=np.float64),
            'leftHipYawPitch': spaces.Box(low=np.array([-90]), high=np.array([1]), dtype=np.float64),
            'rightHipYawPitch': spaces.Box(low=np.array([-120]), high=np.array([120]), dtype=np.float64),
            'leftHipRoll': spaces.Box(low=np.array([-25]), high=np.array([45]), dtype=np.float64),
            'rightHipRoll': spaces.Box(low=np.array([-45]), high=np.array([25]), dtype=np.float64),
            'leftHipPitch': spaces.Box(low=np.array([-25]), high=np.array([100]), dtype=np.float64),
            'rightHipPitch': spaces.Box(low=np.array([-25]), high=np.array([100]), dtype=np.float64),
            'leftKneePitch': spaces.Box(low=np.array([-130]), high=np.array([1]), dtype=np.float64),
            'rightKneePitch': spaces.Box(low=np.array([-130]), high=np.array([1]), dtype=np.float64),
            'leftFootPitch': spaces.Box(low=np.array([-45]), high=np.array([75]), dtype=np.float64),
            'rightFootPitch': spaces.Box(low=np.array([-45]), high=np.array([75]), dtype=np.float64),
            'leftFootRoll': spaces.Box(low=np.array([-45]), high=np.array([25]), dtype=np.float64),
            'rightFootRoll': spaces.Box(low=np.array([-25]), high=np.array([45]), dtype=np.float64),
            'leftShoulderPitch': spaces.Box(low=np.array([-120]), high=np.array([120]), dtype=np.float64),
            'rightShoulderPitch': spaces.Box(low=np.array([-120]), high=np.array([120]), dtype=np.float64),
            'leftShoulderYaw': spaces.Box(low=np.array([-1]), high=np.array([95]), dtype=np.float64),
            'rightShoulderYaw': spaces.Box(low=np.array([-95]), high=np.array([1]), dtype=np.float64),
            'leftArmRoll': spaces.Box(low=np.array([-120]), high=np.array([120]), dtype=np.float64),
            'rightArmRoll': spaces.Box(low=np.array([-120]), high=np.array([120]), dtype=np.float64),
            'leftArmYaw': spaces.Box(low=np.array([-90]), high=np.array([1]), dtype=np.float64),
            'rightArmYaw': spaces.Box(low=np.array([-1]), high=np.array([90]), dtype=np.float64)        
        }),
        'acc': spaces.Box(low=np.array([-100, -100, -100]), high=np.array([100, 100, 100]), dtype=np.float64),
        'gyr': spaces.Box(low=np.array([-800, -800, -800]), high=np.array([800, 800, 800]), dtype=np.float64),
        'ballpos': spaces.Box(low=np.array([0, -61, -61]), high=np.array([50, 61, 61]), dtype=np.float64),
        'leftFootResistance': spaces.Tuple((spaces.Box(low=-0.10, high=0.10, shape=(3,), dtype=np.float64), spaces.Box(low=-245, high=245, shape=(3,), dtype=np.float64))),
        'rightFootResistance': spaces.Tuple((spaces.Box(low=-0.10, high=0.10, shape=(3,), dtype=np.float64), spaces.Box(low=-245, high=245, shape=(3,), dtype=np.float64))),
        'prevAction': spaces.Box(
            np.array([
                [-120.0, -6.109],     #hj1
                [-45.0, -6.109],      #hj2
                [-90.0, -6.109],      #llj1
                [-120.0, -6.109],     #rlj1
                [-25.0, -6.109],      #llj2
                [-45.0, -6.109],      #rlj2
                [-25.0, -6.109],      #llj3
                [-25.0, -6.109],      #rlj3
                [-130.0, -6.109],     #llj4
                [-130.0, -6.109],     #rlj4
                [-45.0, -6.109],      #llj5
                [-45.0, -6.109],      #rlj5
                [-45.0, -6.109],      #llj6
                [-25.0, -6.109],      #rlj6
                [-120.0, -6.109],     #laj1
                [-120.0, -6.109],     #raj1
                [-1.0, -6.109],       #laj2
                [-95.0, -6.109],      #raj2
                [-120.0, -6.109],     #laj3
                [-120.0, -6.109],     #raj3
                [-90.0, -6.109],      #laj4
                [-1.0, -6.109]]),     #raj4
            np.array([
                [120.0, 6.109],      #hj1
                [45.0, 6.109],       #hj2
                [1.0, 6.109],        #llj1
                [120.0, 6.109],      #rlj1
                [45.0, 6.109],       #llj2
                [25.0, 6.109],       #rlj2
                [100.0, 6.109],      #llj3
                [100.0, 6.109],      #rlj3
                [1.0, 6.109],        #llj4
                [1.0, 6.109],        #rlj4
                [75.0, 6.109],       #llj5 
                [75.0, 6.109],       #rlj5
                [25.0, 6.109],       #llj6
                [45.0, 6.109],       #rlj6
                [120.0, 6.109],      #laj1
                [120.0, 6.109],      #raj1
                [95.0, 6.109],       #laj2
                [1.0, 6.109],        #raj2
                [120.0, 6.109],      #laj3
                [120.0, 6.109],      #raj3
                [1.0, 6.109],        #laj4
                [90.0, 6.109]]),     #raj4
                dtype=np.float64),
        'count': spaces.Discrete(1000) # TODO: Definir count. Default até 1000 steps
        })

    def setDone(self, episodeTime: float, endIfFallen: bool):
        """ 
            Sets conditions for episode's end. 
            Default: episodeTime = 5.0 / endIfFallen = True
        """
        self.endEpisodeIfFallen = endIfFallen
        self.episodeTimeLimit = episodeTime

    def stayIdleBeforeKickOff(self):
        while True:
            self.ws.dynamicUpdate()
            if(self.ws.playMode != 0):
                break

    def close(self):
        ...
