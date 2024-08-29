import asyncio
import psycopg

asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())


def CreatTickets():
    with psycopg.Connection.connect(f"dbname=tt user=postgres password=123") as aconn:
        with aconn.cursor() as acur:
            try:
                acur.execute(f"""CREATE TABLE IF NOT EXISTS public.requests(
                    id bigint NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 9223372036854775807 CACHE 1 ),
                    name text COLLATE pg_catalog."default" NOT NULL,
                    status text COLLATE pg_catalog."default" NOT NULL,
                    "timeCreate" timestamp without time zone NOT NULL,
                    source_system text COLLATE pg_catalog."default",
                    "timeToResolve" bigint,
                    CONSTRAINT requests_pkey PRIMARY KEY (id)
                    )

                    TABLESPACE pg_default;

                    ALTER TABLE IF EXISTS public.requests
                    OWNER to postgres;""")
                aconn.commit()
                return True
            except psycopg.errors.UniqueViolation:
                return False


CreatTickets()