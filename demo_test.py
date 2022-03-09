from server.proxy import Proxy
from gym_rcssserver3d.envs.demo_env import DemoEnv
import time
from stable_baselines3 import DQN

proxy = Proxy(3500)
proxy.start()

env = DemoEnv()

time.sleep(5)

ply = proxy.getPlayerObj('6')
env.setPlayer(ply)

env.stayIdleBeforeKickOff()

model = DQN('MlpPolicy', env, verbose=1, tensorboard_log="./tensorboard_test/")
model.learn(total_timesteps=20000)
model.save("DQN_training_model")

#model = DQN.load("DQN_training_model")

obs = env.reset()
while True:
    action, _states = model.predict(obs)
    #print("ACTION: {}".format(action))
    obs, rewards, dones, info = env.step(action)
    if(dones):
        env.reset()
    #env.render()