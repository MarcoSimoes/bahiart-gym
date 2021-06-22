from gym_rcssserver3d.envs.kick_env import KickEnv
import socket

env = KickEnv()

print(env.action_space.sample())