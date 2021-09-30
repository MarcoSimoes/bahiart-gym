from server.proxy import Proxy
from gym_rcssserver3d.envs.kick_env import KickEnv
import socket
import time

proxy = Proxy(3600)
proxy.start()
time.sleep(5)


ply = proxy.getPlayerObj('6')

env = KickEnv(ply)

#print(env.action_space.sample())
#print(env.observation_space.sample())

while True:
    env.ws.dynamicUpdate()
    print(env.optPlayer.getObs())
    #print(env.ws.time)
    #env.step(env.action_space.sample())