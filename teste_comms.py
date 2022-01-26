#TODO: Transformar em um codigo de "treino" padrão para funcionar de exemplo.

from server.proxy import Proxy
from gym_rcssserver3d.envs.demo_env import DemoEnv
import time

proxy = Proxy(3500)
proxy.start()

env = DemoEnv()

time.sleep(5)

ply = proxy.getPlayerObj('1')
env.setPlayer(ply)

env.stayIdleBeforeKickOff()

#action = env.action_space.sample()
episodes = 5 #If you want more than 5 episodes, you must change the match time of your server accordingly.
for episodes in range(1, episodes+1):
    state = env.reset()
    done = False
    score = 0

    while not done:
        #action = env.action_space.sample()
        n_state, reward, done, info = env.step('1')
        score += reward
    print('-----------------Episode:{} Score:{}'.format(episodes, score))

#while True:
#    print(env.observation_space.sample())
#    env.ws.dynamicUpdate()
#    env.optPlayer.checkFallen()
    # print("Tempo de jogo:{}".format(env.ws.time))
    # print("Posição da bola:{}".format(env.optPlayer.ballPolarPos))
    # print("Node:{}".format(env.ws.ballNode))
    # print("Posição da bola:{}".format(env.ws.ballFinalPos))
    # print("Dados do Giroscópio:{}".format(env.optPlayer.gyro))
    # print("Dados do Acelerometro:{}".format(env.optPlayer.acc))
