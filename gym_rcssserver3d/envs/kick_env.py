from server.player import Player
from server.trainer import Trainer
from server.proxy import Proxy
import gym
from gym import error, spaces, utils
from gym.utils import seeding

import numpy as np
import sys
sys.path.append("../../server")

from server import *

class KickEnv(gym.Env):
  metadata = {'render.modes': ['human']}

  optPlayer: Player = None

  def __init__(self):
    
    BallPos = np.array([0.0, 0.0])
    agentPos = np.array([-0.5, 0.0])
    generalTarget = np.array([15.0, 0.0])
    
   # self.action_space = spaces.Box(np.array([-6.0, -3.0, -2.0]), np.array([-5.0, -2.0, -1.0]), dtype=np.float64)
    self.action_space = spaces.Box(
      np.array([
        [-120.0, -6.109],     #hj1 (angle, angular vel) MIN
        [-45.0, -6.109],      #hj2
        [-120.0, -6.109],     #laj1
        [-1.0, -6.109],       #laj2
        [-120.0, -6.109],     #laj3
        [-90.0, -6.109],      #laj4
        [-90.0, -6.109],      #llj1
        [-25.0, -6.109],      #llj2
        [-25.0, -6.109],      #llj3
        [-130.0, -6.109],     #llj4
        [-45.0, -6.109],      #llj5
        [-45.0, -6.109],      #llj6
        [-120.0, -6.109],     #rlj1
        [-45.0, -6.109],      #rlj2
        [-25.0, -6.109],      #rlj3
        [-130.0, -6.109],     #rlj4
        [-45.0, -6.109],      #rlj5
        [-25.0, -6.109],      #rlj6
        [-120.0, -6.109],     #raj1
        [-95.0, -6.109],      #raj2
        [-120.0, -6.109],     #raj3
        [-1.0, -6.109]]),     #raj4
      np.array([
        [120.0, 6.109],      #hj1 (angle, angular vel) MAX
        [45.0, 6.109],       #hj2
        [120.0, 6.109],      #laj1
        [95.0, 6.109],       #laj2
        [120.0, 6.109],      #laj3
        [1.0, 6.109],        #laj4
        [1.0, 6.109],        #llj1
        [45.0, 6.109],       #llj2
        [100.0, 6.109],      #llj3
        [1.0, 6.109],        #llj4
        [75.0, 6.109],       #llj5 
        [25.0, 6.109],       #llj6
        [120.0, 6.109],      #rlj1
        [25.0, 6.109],       #rlj2
        [100.0, 6.109],      #rlj3
        [1.0, 6.109],        #rlj4
        [75.0, 6.109],       #rlj5
        [45.0, 6.109],       #rlj6
        [120.0, 6.109],      #raj1
        [1.0, 6.109],        #raj2
        [120.0, 6.109],      #raj3
        [90.0, 6.109]]),     #raj4
        dtype=np.float64)

    self.observation_space

    #Player should instance every player on the field acording to proxy (import player objects from proxy)


    #Define action and observation space
    #Define episode end condition flags
    

    #self.command = Trainer()  ### Ver com Gabriel a finalidade dessas 3
    # comms = parser.Parser(sock)
    # game = world.World(sock)
    ...
  def step(self, action): # Actions based in numbers passed to the joints. 22 joints total (define which one will be used in each train)
    
    #instance playerConnection()
    #playerConnection.sendActions(action)

    #Inside playerConnection class, create socket to communicate with agentPlayers
    ...
  def reset(self):

    #change playmode?
    
    #Position ball in the center of the field
    #self.command.beamBall(0,0,0)

    #Position Player behind the ball
    #self.command.beamPlayer(optPlayer.getUnum(), "Left", -0.15, 0, 0.3)
    ...
  def render(self, mode='human'): # Run roboviz or any monitor in the screen to show the training
    ...
  
  def setPlayer(self, player: Player):
    self.optPlayer = player

  def close(self):
    ...