#TODO: Transformar em um codigo de "treino" padrão para funcionar de exemplo.

from server.proxy import Proxy
from gym_rcssserver3d.envs.kick_env import KickEnv
import time

proxy = Proxy(3800)
proxy.start()





env = KickEnv()

time.sleep(5)

ply = proxy.getPlayerObj('1')
env.setPlayer(ply)

episodes = 5
for episodes in range(1, episodes+1):
    state = env.reset()
    done = False
    score = 0

    while not done:
        action = env.action_space.sample()
        n_state, reward, done, info = env.step(action,episodes)
        score += reward
    print('-----------------Episode:{} Score:{}'.format(episodes, score))

#print(env.action_space.sample())
#print(env.observation_space.sample())
#env.ws.staticUpdate()
#while True:
#    env.ws.dynamicUpdate()
#    env.optPlayer.checkFallen()
    # print("Tempo de jogo:{}".format(env.ws.time))
    # print("Posição da bola:{}".format(env.optPlayer.ballPolarPos))
    # print("Node:{}".format(env.ws.ballNode))
    # print("Posição da bola:{}".format(env.ws.ballFinalPos))
    # print("Dados do Giroscópio:{}".format(env.optPlayer.gyro))
    # print("Dados do Acelerometro:{}".format(env.optPlayer.acc))
