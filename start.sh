#!/bin/bash

agentDir=/home/mask/workspace/binRT


printf "Running server.... \n"
sleep 1
rcssserver3d &
sleep 1
printf "\n"

printf "Running proxy...."
sleep 1
python3 ./server/runProxy.py &
sleep 1
printf "\n"

printf "Running Agents"
sleep 1
${agentDir}/startAgent.sh 1 localhost 3500
sleep 1
printf "\n"

# echo "Running Optimization"
# sleep 1
# #rodar otimização

