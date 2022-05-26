from bahiart_gym.server.proxy import Proxy
from bahiart_gym.envs.decideKick_env import DecideKickEnv
import gym
import time
from stable_baselines3 import DQN

proxy = Proxy(3800)
proxy.start()

env = DecideKickEnv()

print("-------------------------------")
print("Waiting for agent to connect")
time.sleep(5)

ply = proxy.getPlayerObj('6')
env.setPlayer(ply)

env.stayIdleBeforeKickOff()

model = DQN('MlpPolicy', env, verbose=1)
model.learn(total_timesteps=10000)
model.save("DQN_training_model")

#model = DQN.load("DQN_training_model")

obs = env.reset()
while True:
    action, _states = model.predict(obs)
    #print("ACTION: {}".format(action))
    # obs, rewards, done, info = env.step(action)
    obs, rewards, done, info = env.step(1)
    if(done):
        env.reset()
    #env.render()