import gym
import socket
import subprocess as proc
from gym import error, spaces, utils
from gym.utils import seeding

class Rcssserver3dEnv(gym.Env):
  metadata = {'render.modes': ['human']}

  def __init__(self):                                               #variaveis iniciais como importação do modelo do agente e posicionamento do mesmo. Usar numeros do naosoccersim.rb e spark.rb
    

    #run and connect to server
    #proc.run(["rcssserver3d", "&"])                                #Não consegui achar uma forma de rodar e me liberar o terminal. Melhor rodar o servidor na mão por hora. Ou cria um script.sh pra rodar tudo.
    HOST = 'localhost'
    PORT = 3200
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)        #AF_INET = ipv4 / SOCK_STREAM = TCP
    sock.connect((HOST, PORT))                                      #estudar TCC de edivã, S-Expression

    #receive server state and parse it to the trainer to fill the variables

    
    
    
    
    #send init mensage to server. Set playmode to playOn
    
    msg = "(playMode playOn)"                                       #Constroi a mensagem
    msgLen = socket.htonl(len(msg))                                 #pega o tamanho da mensagem e traduz utilizando o metodo Host To Network Long
    prefix = msgLen.to_bytes(4, 'little')                           #converte o tamanho de inteiro para bytes no formato little, assim como é devolvido pelo servidor.

    fullmsg = str(prefix, "utf-8") + msg                            #concatena o prefixo com a mensagem, transformando o prefixo em string com encode em utf-8, evitando duplicação do "b" de mensagens em bytes

    sock.send(fullmsg.encode())                                     #encoda a mensagem e envia ela pelo socket TCP


    

    
    
    #position player on field

    ...
  def step(self, action):                                           #Todas as ações são baseadas em numeros passados para as articulações. 22 articulações no total (definir quais são usadas pra cada treino)
    ...
  def reset(self):                                                  #condições de finalização da simulação e reset de posicionamento
    ...
  def render(self, mode='human'):                                   #rodar o roboviz ou algum monitor na tela pra desenhar o treino
    ...
  def close(self):
    ...