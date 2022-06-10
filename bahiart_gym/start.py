import os
import subprocess
import time
import sys



def startEnv():
    
    proxyPort=3800
    serverPort=3100
    monitorPort=3200
    #Reading config.ini in current working directory
    cfgfile=open("config.ini","r")
    options=cfgfile.readlines()
    cfgfile.close()
 
    
    for opt in options:
        optsplit = opt.split("=")
        if(optsplit[0]=='TRAINING_COMMAND'):
            trainingCommand=optsplit[1].split("\n")[0].split(" ")
        elif(optsplit[0]=="TEAM_COMMAND"):
            teamCommand=optsplit[1].split("\n")[0]
        elif(optsplit[0]=="TEAM_FOLDER"):
            teamFolder=optsplit[1].split("\n")[0]
        elif(optsplit[0]=="PROXY_PORT"):
            proxyPort=int(optsplit[1].split("\n")[0])
        elif(optsplit[0]=="SERVER_PORT"):
            serverPort=int(optsplit[1].split("\n")[0])
        elif(optsplit[0]=="MONITOR_PORT"):
            monitorPort=int(optsplit[1].split("\n")[0])
    
    trainingCommand.append(str(proxyPort))
    trainingCommand.append(str(serverPort))
    trainingCommand.append(str(monitorPort))
     
    
    serverCommand = "rcssserver3d"
    
    serverProcess = subprocess.Popen(serverCommand)
    
    time.sleep(6)
    
    trainingProcess = subprocess.Popen(trainingCommand)
    
    
    proxyAvailable=False
      
    while not proxyAvailable:
        try:
            output=subprocess.check_output("lsof -i:"+str(proxyPort), shell=True)
            # print("\nOk: ", output.decode("utf-8"),)
            proxyAvailable=True
        except subprocess.CalledProcessError as e:
            # print("\nError: ", e.output.decode("utf-8"))
            pass

    
    cwd = os.getcwd()
    os.chdir(teamFolder)
    subprocess.Popen(teamCommand,cwd=teamFolder, shell=True)
    os.chdir(cwd)
    
    
    
#Main Function

if __name__ == '__main__':
    startEnv()
    
    
   