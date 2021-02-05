# Aqui no env, ao invés de criar um ambiente para cada objetivo, como o "kick" ou "walk", pensei em
# deixar um ambiente só, com as mesmas ações e a pessoa que quiser treinar usa da forma que julgar
# necessário. No caso, como ações(step), podemos utilizar o código em c, como vc havia falado, e ter a 
# possibilidade de mandar ações através das juntas que desejamos movimentar. 
# Aí talvez seja útil implementar o polimorfismo, caso seja necessário (um com o código c e outro com a 
# movimentação das juntas, que é um nível mais baixo para a ação)

import gym
import socket
import subprocess as proc
from gym import error, spaces, utils
from gym.utils import seeding

class KickEnv(gym.Env):
  self.metadata = {'render.modes': ['human']}

  def __init__(self): #variaveis iniciais como importação do modelo do agente e posicionamento do mesmo. Usar numeros do naosoccersim.rb e spark.rb
    

    #run and connect to server
    self.proc.run('rcssserver3d')
    self.HOST = 'localhost'
    self.PORT = 3100
    self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    self.sock.connect((HOST, PORT))

    ...
  def step(self, action): #Todas as ações são baseadas em numeros passados para as articulações. 22 articulações no total (definir quais são usadas pra cada treino)
    ...
  def reset(self): #condições de finalização da simulação e reset de posicionamento
    ...
  def render(self, mode='human'): #rodar o roboviz ou algum monitor na tela pra desenhar o treino
    ...
  def close(self):
    ...