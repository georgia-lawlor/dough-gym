from gym.envs.registration import register

register(
    id='basic-v0',
    entry_point='dough_gym.envs:BasicEnv',
)

register(
    id='basic-v2',
    entry_point='douhg_gym.envs:BasicEnv2',
)