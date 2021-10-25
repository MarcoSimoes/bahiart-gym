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

class KickEnv(gym.Env):
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
      
      #Calculate reward (EXTRA: -2 each goal taken, +4 each goal scored)
      ballDistanceDiff = currBallPos - self.initBallPos
      if(ballDistanceDiff <= 0):
        reward += -1
      elif(ballDistanceDiff > 0 and ballDistanceDiff < 0.1):
        reward += 0
      elif(ballDistanceDiff > 0.1):
        reward = (ballDistanceDiff/0.1)*2 #Not summing. Otherwise it would keep adding until the time was up. I only want the last.
      
      #Verify if episode is done
      if(elapsedTime > 5 and self.ws.ballSpeed < 0.005):
        done = True
        if(ballDistanceDiff < 0.001):
          reward += -5
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
    
    #if ready = 1:
      
      #Verifica de o step = done.
      #Return.

    #print(file)


    #get agent->ballPos: self.state + ballpos
    
    #calculate reward: finalpos - initial pos
    

    #Return self.state, reward, done, info    
    ...
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
    # void AgentActions::directKick
    # void AgentActions::dynamicKickToTarget
    # void AgentActions::kickToTarget
    # void AgentActions::goToShootPoint
    # void AgentActions::moveBalltoTarg
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
      'angleAux':"Diferença entre o ângulo/orientação/direção do alvo final e da posição do jogador, que neste caso tem que ser menor do que 5.",
      'clearToDirectKick':"Calculada (ver:AgentActions.cpp)",
      'clearToLongKick':"Calculada (ver:AgentActions.cpp)",
      'isBallInFront':"ws->theirGoalPos.getDistanceTo(ws->ball->position.to2d()) < ws->theirGoalPos.getDistanceTo(ws->me->position.to2d());",
      'lastDynamickKick':"Tempo de execução do último DynamicKick.",
      'maxdist':4.0,
      'mindist':9.0, 
      'theirGoalInterceptionPoint':"lMeBall.getIntersection(lTheirGoal);",
      'targetToBallDist':"targetPosition.to2d().getDistanceTo(ballPos)",
      'oppDist'[12]:"np.array() getOpponentPlayer(x)->position.to2d().getDistanceTo(ballPos)",
      'playerToBallDist':"WorldState::getRelativeToMe(ws→ballPos.to2d())    Vector WorldState::getRelativeToMe(Vector pos) const {return pos - me->position.to2d();}"
    })

  def close(self):
    ...