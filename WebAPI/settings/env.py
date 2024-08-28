from environs import Env


async def settings_data(name):
    env = Env()
    env.read_env('settings.txt')
    return env(name)
