# -*- coding: utf-8 -*-
import os
import signal
def killEnv(serverPID, envPID, teamPID):
    
    print("Killing server ...\n")
    os.kill(serverPID, signal.SIGKILL)
    print("Killing environment ...\n")
    os.kill(envPID, signal.SIGTERM)
    print("Killing team ...\n")
    os.kill(teamPID, signal.SIGTERM)