import os
import subprocess
import threading
import time

cfgfile=open("config.ini","r")

options=cfgfile.readlines()
cfgfile.close()

for opt in options:
    optsplit = opt.split("=")
    if(optsplit[0]=='TRAINING_COMMAND'):
        trainingCommand=optsplit[1].split("\n")[0].split(" ")
    elif(optsplit[0]=="TEAM_COMMAND"):
        teamCommand=optsplit[1].split("\n")[0]

serverCommand = "rcssserver3d"

serverProcess = subprocess.Popen(serverCommand)

time.sleep(6)

trainingProcess = subprocess.Popen(trainingCommand)

time.sleep(10)

# teamProcess = subprocess.Popen(teamCommand)
os.system(teamCommand)

time.sleep(60)

# trainingProcess.terminate()
# teamProcess.terminate()
# serverProcess.terminate()
# serverProcess.kill()
















# print("-- Program starting --")

# os.system("kill $(ps aux | grep "+ str(trainingCommand[-1].split("/")[-1])+" | grep -v grep | awk ' { print $2;}')")

# ret = subprocess.check_output("ps ax | grep "+ str(trainingCommand[-1].split("/")[-1])+" | grep -v grep | awk ' { print $1;}'",shell=True).decode("utf-8")

# lineFilter = ret.split("/n")

# toKill = ret.split(" ")[5]

# print(toKill)
# print("> Killing " + str(toKill))
# print(ret)

# processId = ''
# for line in ret:
#     try:
#         processId = line.split(' ')[4]
#         print("Killing processId : " + str(processId))
#         subprocess.run("kill -9 " + str(processId),capture_output=True)
#     except:
#         pass


# ret = ret.split("\n")

# print("> Killing team")

# os.system("~rafael/acso/bahiart/kill.sh")

# print("> Killing rcssserver3d")

# os.system("killall -9 rcssserver3d")





