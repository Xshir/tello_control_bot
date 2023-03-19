from credentials import db_creds
import asyncpg

async def query_db(query: str, fetch=False):
    # postgres://user:password@host:port/database?option=value
    database_access_url = f"postgres://{db_creds['user']}:{db_creds['password']}@{db_creds['host']}:{db_creds['port']}/{db_creds['database']}"
   
    try:
        pool = await asyncpg.create_pool(
            database_access_url
        )  # creates a pool to acquire and connect to later
        print("POSTGRESQL connected = ", pool)
    except Exception as e:
        print("Something went wrong: ", e)

        async with pool.acquire() as conn:
            if fetch is False:
             await conn.execute(query)
            elif fetch is True:
             record = await conn.fetch(query)
             return record