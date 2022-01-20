from gym.spaces import box, space
from numpy.core.fromnumeric import shape
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

class decideKick_env(gym.Env):
  metadata = {'render.modes': ['human']}

  optPlayer: Player = None

  def __init__(self, player: Player):
    
    #CREATING WORLD OBJECT AND UPDATING ITS VARIABLES
    self.command = Trainer()
    self.ws = World()
    self.ws.staticUpdate()
    self.ws.dynamicUpdate()

    self.generalTarget = np.array([15.0, 0.0, 0.0])   #DEFAULT: Enemy Goal (considering the agent is in the middle of the field)
    self.episodeInitTime = None
    self.initBallPos = None
    
    self.setPlayer(player)  
    self.createActionSpace()
    self.createObservationSpace()

    self.state = player.getObs()

    #Define episode end condition flags
    self.maxKickTime = 5                              #DEFAULT: 5 seconds
    self.kickThreshold = 1                            #DEFAULT: 1 meter radius
    self.minBallSpeed = 0.05

    #Episode ending conditions: Time + Ball speed close to 0 / player fell + Ball speed close to 0 / Ball outside kick threshold (1 meter) + ball speed close to 0
    
    
    #self.state = self.ballInitPos

    ...
  def step(self, action): # Actions based in numbers passed to the joints. 22 joints total (define which one will be used in each train)
    
    self.command.reqFullState()
    self.ws.dynamicUpdate()
    #DEBUG
    print("BallPOS: {}".format(self.ws.ballFinalPos))
    print("BALLSPEED: {}".format(self.ws.ballSpeed))
    print("TIME: {}".format(self.ws.time))
    #FIMDEBUG
    if(self.episodeInitTime == None):
      self.episodeInitTime = self.ws.time
    if(self.initBallPos == None):
      self.initBallPos = self.ws.ballFinalPos[0] #TODO: Corrigir esse ballpos. Verificar novamente o node, mandar printar len pra ver se estou pegando o node correto. Comparar logica do gamemonitor.py de Marco
    reward = 0

    # 1 - Write the actions into another file for the team to collect.
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
    
    # 1 - Write 0 into a ready file to let the team know the actions are ready to be executed.
    ready = open("/home/mask/workspace/ready.txt", "w")
    ready.write('0')
    ready.close()
  
    #Keep waiting for team to execute step
    ready = open("/home/mask/workspace/ready.txt", "r")
    readyFile = ready.read()
    ready.close()
    while(readyFile == '0'):
      #time.sleep(1)
      ready = open("/home/mask/workspace/ready.txt", "r")
      readyFile = ready.read()
      ready.close()
      #DEBUGS
      #print("PRESO NO WHILE: {}".format(readyFile))
    
    #Check if the team executed the action and proceed.
    if(readyFile == '1'):
      #Update world and observation information
      self.ws.dynamicUpdate()
      currBallPos = self.ws.ballFinalPos[0]
      currTime = self.ws.time
      elapsedTime = currTime - self.episodeInitTime
      self.state = self.optPlayer.getObs() # + action space + count
      
      reward = calculateReward()
      
      if(episodeDone()):
        done = True
        self.initBallPos = None
        self.episodeInitTime = None
      else:
        done = False
      

      info = {}
      #DEBUGS
      print("CHEGOU NO FIM. RESULTADOS: ")
      print("NoneState:{} reward:{} done:{} info:{}".format((self.state == None), reward, done, info))  
      #FIMDEBUGS
      return self.state, reward, done, info
    
    else:
      print("ERRO NO READY: {}".format(readyFile))
      return self.state, 0, False, {}
    
  # TODO reset conditions
  def reset(self):
    
    self.ws.dynamicUpdate()
    
    #Place the ball in the center of the field
    self.command.beamBall(0.0, 0.0, 0.0)

    #Place the Player behind the ball
    self.command.beamPlayer(self.optPlayer.getUnum(), "Left", -0.2, 0, 0.3)

    self.state = self.optPlayer.getObs()

    return self.state

  def render(self, mode='human'): # Run roboviz or any monitor in the screen to show the training
    ...

  
  def setPlayer(self, player: Player):
    self.optPlayer = player

  def createActionSpace(self):
        # TODO ver agent actions
        # -1 - CarryBall
        # -2 - Long Kick
        # -3 - Dynamic Kick
        # -4 - Direct Kick
        self.action_space = spaces.Discrete(4)

  def createObservationSpace(self):
    self.observation_space = spaces.Dict({
      'aliesArray':"x,y, z e orientação dos aliados",
      'opponentsArray':"x,y, z e orientação dos oponentes",
      'ballPos':"x,y, z da bola",
      'mePos':"x,y, z e orientação do ativo",
      'target':"x,y, z e orientação do alvo",
      'playMode':"Playmode definido no server"
    })

  def close(self):
    ...

  def episodeDone(self):
    if(self.ws.time > 20):
      return True
    if(ballWithEnemy()):
      return True
    if(ballOutsideTheField()):
      return True
    if((self.ws.scoreLeft != 0) and (self.ws.scoreRight != 0)):
      return True
    # TODO ball pos inside target radius(0,5 meters)
    # if()
    if()

  # TODO return true or false - Ball is with the enemy?
  def ballWithEnemy(self):
    ...

  # TODO return true or false - Ball is outside the field
  def ballOutsideTheField(self):
    ...
  
  def ballWithOurTeam(self):
    ...

  def calculateReward(self):
    reward = 0
    if(ballWithOurTeam()):
      reward+=1
    if(self.ws.scoreRight != 0):
      # TODO see if right is our team
      reward+=5
    if(self.ws.scoreLeft != 0):
      # TODO see if left is opponent team
      reward-=5
    if(ballWithEnemy()):
      reward-=2
    # TODO reward distance variation ball
    # distanciaPercorrida = Distância percorrida em direção ao target ou contra otarget(distância inicial - distância atual)
    # distanciaInicial = Distancia inicial da bola para o target
    # distancia atual = distância da bola ao target no final de cada step
    # reward+=(3*(distanciaPercorridaBola/distanciaInicialBola))