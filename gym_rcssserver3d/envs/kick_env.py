import gym
import socket
import subprocess as proc
from gym import error, spaces, utils
from gym.utils import seeding

class KickEnv(gym.Env):
  metadata = {'render.modes': ['human']}

  def __init__(self): #variaveis iniciais como importação do modelo do agente e posicionamento do mesmo. Usar numeros do naosoccersim.rb e spark.rb
    

    #run and connect to server
    proc.run('rcssserver3d')
    HOST = 'localhost'
    PORT = 3100
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((HOST, PORT))

    ...
  def step(self, action): #Todas as ações são baseadas em numeros passados para as articulações. 22 articulações no total (definir quais são usadas pra cada treino)
    ...
  def reset(self): #condições de finalização da simulação e reset de posicionamento
    ...
  def render(self, mode='human'): #rodar o roboviz ou algum monitor na tela pra desenhar o treino
    ...
  def close(self):
    ...