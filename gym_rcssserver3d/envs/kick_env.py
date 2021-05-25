import gym
from gym import error, spaces, utils
from gym.utils import seeding

from server.trainer import Trainer

class KickEnv(gym.Env):
  metadata = {'render.modes': ['human']}

  def __init__(self):
    
    #Instance World, Player (how to run a while to keep theese two updated??)

    #Player should instance every player on the field acording to proxy (import player objects from proxy)


    #Define action and observation space
    #Define episode end condition flags
    

    self.command = Trainer() ### Ver com Gabriel a finalidade dessas 3
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
    self.command.beamBall(0,0,0)

    #Position Player behind the ball
    self.command.beamPlayer(1, "Left", -0.15, 0, 0.3)
    ...
  def render(self, mode='human'): # Run roboviz or any monitor in the screen to show the training
    ...
  def close(self):
    ...