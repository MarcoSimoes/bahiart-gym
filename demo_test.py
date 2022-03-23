from bahiart_gym.server.proxy import Proxy
from bahiart_gym.envs.demo_env import DemoEnv
from stable_baselines3 import DQN
import time

proxy = Proxy(3800)                                         #Importa o proxy que será utilizado para vincular o agente ao servidor na porta especificada.
proxy.start()                                               #Inicia o proxy

env = DemoEnv()                                             #Instancia o ambiente de demonstração

time.sleep(5)                                               #Espera 5 segundos. Isso é apenas para garantir que o agente seja manualmente inicializado a tempo.

ply = proxy.getPlayerObj('6')                               #Recupera o objeto gerado pelo proxy para o agente especificado para o treinamento.
env.setPlayer(ply)                                          #Define o objeto do agente dentro do ambiente.

env.stayIdleBeforeKickOff()                                 #Mantém o ambiente estático enquanto o playmode for "before kick off"

model = DQN('MlpPolicy', env, verbose=1)                    #Define o modelo de treinamento como DQN.
model.learn(total_timesteps=10000)                          #Inicia o aprendizado. A variavel "total_timesteps" define em quantos steps o aprendizado será realizado
model.save("DQN_training_model")                            #Após o final do aprendizado, salva o modelo em um arquivo com o nome especificado.

#model = DQN.load("DQN_training_model")                     #O modelo também pode ser iniciado diretamente com uma rede já treinada utilizando a função load("nome_do_arquivo_de_treinamento_salvo")

obs = env.reset()                                           #Reseta o ambiente, colocando o agente e a bola em suas posições iniciais.
while True:
    action, _states = model.predict(obs)                    #Agora que o treinamento ja foi concluido, esse scripts irá utilizar a rede neural para gerar as ações que serão utilizadas pelo agente.
    obs, rewards, dones, info = env.step(action)            #Aqui a função step envia a ação para o agente e espera ele a executar.
    if(dones):
        env.reset()                                         #Toda vez que o episodio terminar, a função reset é chamada, reposicionando o agente e a bola.