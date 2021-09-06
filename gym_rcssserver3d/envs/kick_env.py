from server.player import Player
from server.trainer import Trainer
from server.proxy import Proxy
from server.world import World
import gym
from gym import error, spaces, utils
from gym.utils import seeding

import numpy as np
import sys, time
sys.path.append("../../server")

from server import *

class KickEnv(gym.Env):
  metadata = {'render.modes': ['human']}

  optPlayer: Player = None

  def __init__(self):
    
    #CREATING WORLD OBJECT AND UPDATING ITS VARIABLES
    self.ws = World()
    self.ws.staticUpdate()
    self.ws.dynamicUpdate()

    self.generalTarget = np.array([15.0, 0.0, 0.0])   #DEFAULT: Enemy Goal (considering the agent is in the middle of the field)
    
    self.createActionSpace()
    # CREATEOBSERVATIONSPACE()

    #Define episode end condition flags
    self.maxKickTime = 5                              #DEFAULT: 5 seconds
    self.kickThreshold = 1                            #DEFAULT: 1 meter radius
    #Episode ending conditions: Time + Ball speed close to 0 / player fell + Ball speed close to 0 / Ball outside kick threshold (1 meter) + ball speed close to 0
    
    
    #self.state = self.ballInitPos

    ...
  def step(self, action): # Actions based in numbers passed to the joints. 22 joints total (define which one will be used in each train)
    
    #self.ws.dynamicUpdate()
    #Apply Action: write file
    #Calculate reward:
    #check if episode is done:
    #return step information:

    #use data from optPlayer

    myList = []

    for i in range(0, len(action)):
      for j in range(0, len(action[i])):
        myList.append(action[i,j])

    #toPrint = str(myList)
    file = open("/home/mask/workspace/gymOut.txt", "w").close() #Creating a file if not existing
    file = open("/home/mask/workspace/gymOut.txt", "a")
    
    for value in myList:
      file.write(str(value))
      file.write(',')
    
    file.close()
    #print(file)

    #sleep for maxKickTime
    #time.sleep(self.maxKickTime)

    #get agent->ballPos: self.state + ballpos
    
    #calculate reward: finalpos - initial pos
    # +1 - each 0.1 positive distance on X, -1 each 0.1 negative distance on X, -2 each goal taken, +2 each goal scored
    self.info = {}

    #Return self.state, reward, done, info    
    ...
  def reset(self):

    self.command = Trainer()

    self.ws.dynamicUpdate()
    self.startTime = self.ws.time
    
    #Place the ball in the center of the field
    self.command.beamBall(0.0, 0.0, 0.0)

    #Place the Player behind the ball
    self.command.beamPlayer(self.optPlayer.getUnum(), "Left", -0.5, 0.0)
    #self.command.beamPlayer(self.optPlayer.getUnum(), "Left", -0.15, 0, 0.3)

    #wait 1 second just to make sure everything will be beamed correctly
    

    self.ballInitPos = self.optPlayer.getBallPos() #returns Distance, Angle1, Angle2
    
    #MUST IMPLEMENT THIS 
    #self.agentInitPos = self.optPlayer.getSelfPos()

    self.state = self.ballInitPos

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

  def createObservationSpace(self, player):
    self.observation_space = spaces.Box(
      np.array(

      ),
      np.array(

      ),
      dtype=np.float64)

  def close(self):
    ...