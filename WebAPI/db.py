import asyncio
import psycopg
from settings.env import settings_data

asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())


async def CreatRequest(name, status, TimeCreate, TimeToResolve, SourceSystem):
    async with await psycopg.AsyncConnection.connect(f"dbname=tt user=postgres password=123") as aconn:
        async with aconn.cursor() as acur:
            try:
                await acur.execute(f"""INSERT INTO requests (name, status, "timeCreate", "timeToResolve")
                                VALUES (%s, %s, %t, %t, %s);""", (name, status, TimeCreate, TimeToResolve, SourceSystem))
                await aconn.commit()
                return True
            except psycopg.errors.UniqueViolation:
                return False
