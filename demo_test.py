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
from bahiart_gym.server.proxy import Proxy
from bahiart_gym.envs.demo_env import DemoEnv
import gym
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

print("Starting proxy in port ",proxyPort," connecting to port ",serverPort)
proxy = Proxy(proxyPort,serverPort)
proxy.start()
print("\nStarting DemoEnv in monitorPort ",monitorPort,"\n")
env = DemoEnv(monitorPort)

print("-------------------------------")
print("> Waiting for agent to connect")


ply = proxy.getPlayerObj('6')

while(ply == None):
    time.sleep(0.5)
    ply = proxy.getPlayerObj('6')

env.setPlayer(ply)

env.stayIdleBeforeKickOff()

# model = DQN('MlpPolicy', env, verbose=1)
# model.learn(total_timesteps=10000)
# model.save("DQN_training_model")

#model = DQN.load("DQN_training_model")

obs = env.reset()
while True:
    #action, _states = model.predict(obs)
    #print("ACTION: {}".format(action))
    obs, rewards, dones, info = env.step(2)
    if(dones):
        env.reset()
    #env.render()