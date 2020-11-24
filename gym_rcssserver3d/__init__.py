from gym.envs.registration import register

register(
    id='rcssserver3d-v0',
    entry_point='gym_rcssserver3d.envs:Rcssserver3dEnv',
)
register(
    id='kick-v0',
    entry_point='gym_rcssserver3d.envs:KickEnv',
)
register(
    id='walk-v0',
    entry_point='gym_rcssserver3d.envs:WalkEnv',
)