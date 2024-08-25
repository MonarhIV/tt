from environs import Env


async def settings_data(name: str):
    env = Env()
    env.read_env('settings.txt')
    return env.srt(name)
