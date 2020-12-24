import parser
import trainer
import comms
#from connection import sParser, comand, Conection

net = comms.Comms()

while True:
    net.updateSExp()
    tempo = net.sParser.getValue('time', net.sParser.parsedExp)
    if tempo != None:
        print(tempo)