import gym
import socket
import sexpr
import trainer
import parser
import world
#import subprocess as proc                                          ##Não consegui achar uma forma de rodar e me liberar o terminal. Melhor rodar o servidor na mão por hora. Ou cria um script.sh pra rodar tudo.
from gym import error, spaces, utils
from gym.utils import seeding

class Rcssserver3dEnv(gym.Env):
  metadata = {'render.modes': ['human']}

  def __init__(self):                                              #Initial variables, such as agent model and position import. Use naosoccersim.rb and spark.rb numbers
                                   
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
  def step(self, action): # Actions based in numbers passed to the joints. 22 joints total (define which one will be used in each train)
    ...
  def reset(self): # Ending conditions for the simulation and reset position.
    ...
  def render(self, mode='human'): # Run roboviz or any monitor in the screen to show the training
    ...
  def close(self):
    ...