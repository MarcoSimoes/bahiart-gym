from gym.envs.registration import register

# register(
#     id='kick-v0',
#     entry_point='bahiart_gym.envs:KickEnv',
# )
register(
    id='demo-v0',
    entry_point='bahiart_gym.envs:DemoEnv'
)
# register(
#     id='decideKick-v0',
#     entry_point='bahiart_gym.envs:DecideKickEnv'
# )