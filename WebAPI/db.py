import asyncio
import psycopg
from settings.env import settings_data

asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())


async def CreatTickets(name, status, TimeCreate, TimeToResolve, SourceSystem):
    async with await psycopg.AsyncConnection.connect(f"dbname=tt user=postgres password=123") as aconn:
        async with aconn.cursor() as acur:
            try:
                await acur.execute(f"""INSERT INTO requests (name, status, "timeCreate", "source_system", "timeToResolve")
                                VALUES (%s, %s, %t, %s, %b);""", (name, status, TimeCreate, SourceSystem, TimeToResolve))
                await aconn.commit()
                return True
            except psycopg.errors.UniqueViolation:
                return False


async def clientResponse():
    async with await psycopg.AsyncConnection.connect("dbname=tt user=postgres password=123") as aconn:
        async with aconn.cursor() as acur:
            await acur.execute(f"""SELECT * FROM requests WHERE source_system = 'client'""")
            d = await acur.fetchall()
            return d

