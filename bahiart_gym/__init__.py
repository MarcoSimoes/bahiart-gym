from gym.envs.registration import register

register(
    id='demo-v0',
    entry_point='bahiart_gym.envs:DemoEnv'
)