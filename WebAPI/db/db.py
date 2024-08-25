import asyncio
import psycopg
from ..settings.env import settings_data

asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())


async def CreatRequest(name, status, TimeCreate, TimeToResolve):
    async with await psycopg.AsyncConnection.connect(
            f"dbname={settings_data('dbname')} user={settings_data('user')} password={settings_data('password')}") as aconn:
        async with aconn.cursor() as acur:
            try:
                await acur.execute(f"""INSERT INTO requests (name, status, timeCreate, timeToResolve)
                                VALUES ('{name}', '{status}', {TimeCreate}, {TimeToResolve});""")
                await aconn.commit()
                return True
            except psycopg.errors.UniqueViolation:
                return False
