"""
        Copyright (C) 2022  Salvador, Bahia
        Gabriel Mascarenhas, Marco A. C. Simões, Rafael Fonseca

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
from stable_baselines3 import DQN

proxy = Proxy(3800)                                                     #Imports the proxy that will be used to bind the agent to the server at the specified port. Change the number as you please, but remember it when launching your agent.
proxy.start()                                                           #Starts the proxy.

env = DemoEnv()                                                         #Creates a demo env instance.

input("Press any key once the agent is connected to the server...")     #Simple input so the environment will wait for the agent. Remember to use the proxy port you previously chose instead of the default 3100.

ply = proxy.getPlayerObj('6')                                           #Gets the player object created by the proxy. Change the number 6 according to the one of your agent.
env.setPlayer(ply)                                                      #Defines the retrieved object inside the environment.

env.stayIdleBeforeKickOff()                                             #Keeps the environment idle during the 'beforeKickOff' playmode so you can start it at any time by clicking B or K on the Roboviz screen.

model = DQN('MlpPolicy', env, verbose=1)                                #Defines the training model as DQN.
model.learn(total_timesteps=10000)                                      #Starts learning. The "total_timesteps" variable defines how many steps the learning will take.
model.save("DQN_training_model")                                        #After the learning is done, this saves the model in a file with the given name.

#model = DQN.load("DQN_training_model")                                 #The model can also be initialized with an already trained network using the load("trained_model_file") function.

obs = env.reset()                                                       #Resets the environment, beaming the agent and the ball to predefined initial positions.
while True:
    action, _states = model.predict(obs)                                #Now that the training is over, this script function will generate actions based on the trained model network.
    obs, rewards, dones, info = env.step(action)                        #Here, the step function sends the action to the agent and waits its execution.
    if(dones):
        env.reset()                                                     #At the end of every episode, the environment is reset.