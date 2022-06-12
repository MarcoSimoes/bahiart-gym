"""
        Copyright (C) 2022  Salvador, Bahia
        Gabriel Mascarenhas, Marco A. C. Simões, Rafael Fonseca

        This file is part of BahiaRT GYM.

        BahiaRT GYM is free software: you can redistribute it and/or modify
        it under the terms of the GNU Affero General Public License as
        published by the Free Software Foundation, either version 3 of the
        License, or (at your option) any later version.

        BahiaRT GYM is distributed in the hope that it will be useful,
        but WITHOUT ANY WARRANTY; without even the implied warranty of
        MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
        GNU Affero General Public License for more details.

        You should have received a copy of the GNU Affero General Public License
        along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
#This demo environment was designed to be used with just a single agent.
#Remember to run the rcssserver3d and RoboViz(or any other monitor) before running this script.
from bahiart_gym.server.proxy import Proxy
from bahiart_gym.envs.demo_env import DemoEnv
import time
import sys
from stable_baselines3 import DQN


proxyPort=3800
serverPort=3100
monitorPort=3200
                                                     
if(len(sys.argv) > 1):
    proxyPort=int(sys.argv[1])
    
if(len(sys.argv) > 2):
    serverPort=int(sys.argv[2])

if(len(sys.argv) > 3):
    monitorPort=int(sys.argv[3])

print("Starting proxy in port: ",proxyPort," | Connecting to port: ",serverPort)
proxy = Proxy(proxyPort,serverPort)                                             #Create the proxy that will be used to bind the agent to the server at the specified port. Change the number in config.ini, as you please, but remember it when launching your agent.
proxy.start()                                                                   #Starts the proxy.
print("\nStarting DemoEnv in monitorPort: ",monitorPort,"\n")
env = DemoEnv(monitorPort)                                                      #Creates a demo env instance.


print("-------------------------------")
print("> Waiting for agent to connect")


ply = proxy.getPlayerObj('6')                                                   #Gets the player object created by the proxy. Change the number 6 according to the one of your agent.


while(ply == None):                                                             # Keeps waiting until agent 6 connects
    time.sleep(0.5)
    ply = proxy.getPlayerObj('6')

env.setPlayer(ply)                                                              #Defines the retrieved object inside the environment.

env.stayIdleBeforeKickOff()

model = DQN('MlpPolicy', env, verbose=1)
model.learn(total_timesteps=10000)
model.save("DQN_training_model")

model = DQN.load("DQN_training_model")
action = 2
obs = env.reset()                                                               #Resets the environment, beaming the agent and the ball to predefined initial positions.
while True:
    action, _states = model.predict(obs)
    print("ACTION: {}".format(action))
    obs, rewards, dones, info = env.step(action)
    if(dones):
        env.reset()                                                             #At the end of every episode, the environment is reset.
    #env.render()