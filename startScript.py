import os
import subprocess
import threading
import time

serverCommand = "rcssserver3d"
gymCommand = ["python3","/home/rafael/acso/bahiart-gym/demo_test.py"]
teamCommand = ["acso/bahiart/startAgent.sh", "6" ,"localhost" ,"3800", "demo"]

def runCommand(command):
    subprocess.run(command)

print("Program starting")

ret = ""
ret = subprocess.check_output("ps aux | grep python3",shell=True).decode("utf-8")

ret = ret.split("\n")

print("> Killing team")


os.system("~rafael/acso/bahiart/kill.sh")

print("> Killing rcssserver3d")

os.system("killall -9 rcssserver3d")

print("> Killing Python3")

processId = ''
for line in ret:
    try:
        processId = line.split(' ')[4]
        print("Killing processId : " + str(processId))
        subprocess.run("kill -9 " + str(processId),capture_output=True)
    except:
        pass

serverProcess = subprocess.Popen(serverCommand)

time.sleep(10)

gymProcess = subprocess.Popen(gymCommand)

time.sleep(6)

teamProcess = subprocess.Popen(teamCommand)

time.sleep(20)

gymProcess.terminate()
teamProcess.terminate()
serverProcess.terminate()