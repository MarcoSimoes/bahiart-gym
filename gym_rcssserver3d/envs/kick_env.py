import gym
import socket
import subprocess as proc
from gym import error, spaces, utils
from gym.utils import seeding

class KickEnv(gym.Env):
  metadata = {'render.modes': ['human']}

  def __init__(self): #Initial variables, such as agent model and position import. Use naosoccersim.rb and spark.rb numbers
    

    #run and connect to server
    proc.run('rcssserver3d')
    HOST = 'localhost'
    PORT = 3100
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((HOST, PORT))

    ...
  def step(self, action): # Actions based in numbers passed to the joints. 22 joints total (define which one will be used in each train)
    ...
  def reset(self): # Ending conditions for the simulation and reset position.
    ...
  def render(self, mode='human'): # Run roboviz or any monitor in the screen to show the training
    ...
  def close(self):
    ...