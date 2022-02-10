#TODO: Transformar em um codigo de "treino" padrão para funcionar de exemplo.

from server.proxy import Proxy
from gym_rcssserver3d.envs.demo_env import DemoEnv
import time
from stable_baselines3 import PPO
# from stable_baselines.common.policies import MlpPolicy
# from stable_baselines import PPO2

proxy = Proxy(3500)
proxy.start()

env = DemoEnv()

time.sleep(5)

ply = proxy.getPlayerObj('1')
env.setPlayer(ply)

env.stayIdleBeforeKickOff()

#model = PPO2(MlpPolicy, env, verbose=1)
model = PPO("MlpPolicy", env, verbose=1)
model.learn(total_timesteps=100)
model.save("./demo_training_model")
print("--------------Fim do Learn!---------------")

obs = env.reset()
while True:
    action, _states = model.predict(obs)
    print("ACTION: {}".format(action))
    obs, rewards, dones, info = env.step(action)
    print("---------------Fim do While---------------")
    #env.render()
