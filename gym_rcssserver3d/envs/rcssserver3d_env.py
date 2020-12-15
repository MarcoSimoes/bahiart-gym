import gym
import socket
import sexpr
import trainer
import parser
import world
#import subprocess as proc                                          #Não consegui achar uma forma de rodar e me liberar o terminal. Melhor rodar o servidor na mão por hora. Ou cria um script.sh pra rodar tudo.
from gym import error, spaces, utils
from gym.utils import seeding

class Rcssserver3dEnv(gym.Env):
  metadata = {'render.modes': ['human']}

  def __init__(self):                                               #variaveis iniciais como importação do modelo do agente e posicionamento do mesmo. Usar numeros do naosoccersim.rb e spark.rb
                                   
    HOST = 'localhost'
    PORT = 3200
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)        #AF_INET = ipv4 / SOCK_STREAM = TCP
    sock.connect((HOST, PORT))                                      #estudar TCC de edivã, S-Expression

    comand = trainer.Trainer(sock)
    comms = parser.Parser(sock)
    game = world.World(sock)
    
    #receive server state and parse it to the trainer to fill the variables

    #playMode = comms.getValue('play_mode', comms.sexp)
    
    
    #send init mensage to server. Set playmode to playOn
    
    #comand.changePlayMode("PlayOn")


    

    
    
    #position player on field

    ...
  def step(self, action):                                           #Todas as ações são baseadas em numeros passados para as articulações. 22 articulações no total (definir quais são usadas pra cada treino)
    ...
  def reset(self):                                                  #condições de finalização da simulação e reset de posicionamento
    ...
  def render(self, mode='human'):                                   #rodar o roboviz ou algum monitor na tela pra desenhar o treino
    ...
  def close(self):
    ...