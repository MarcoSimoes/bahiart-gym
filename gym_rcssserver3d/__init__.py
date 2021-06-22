from gym.envs.registration import register

register(
    id='kick-v0',
    entry_point='gym_rcssserver3d.envs:KickEnv',
)
