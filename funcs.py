from credentials import db_creds
import asyncpg

# postgres://user:password@host:port/database?option=value
database_access_url = f"postgres://{db_creds['user']}:{db_creds['password']}@{db_creds['host']}:{db_creds['port']}/{db_creds['database']}"

async def query_db(query: str, fetch=False):
    
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

async def retrieve_tello_instructions_in_list(pool, tello: str) -> list:
    # postgres://user:password@host:port/database?option=value
   
    list_of_instructions = []

    async with pool.acquire() as conn:
            records = await conn.fetch(f"SELECT * FROM tello_table")
            await conn.close()
            for column in records:
                if column[tello] is not None:
                    if ":" not in column[tello]:
                        list_of_instructions.append(column[tello])

            
            return list_of_instructions
    
async def start_db():
    try:
        database_access_url = f"postgres://{db_creds['user']}:{db_creds['password']}@{db_creds['host']}:{db_creds['port']}/{db_creds['database']}"
        pool = await asyncpg.create_pool(
            database_access_url
        )  # creates a pool to acquire and connect to later
        print("POSTGRESQL connected = ", pool)
        return pool
    except Exception as e:
        print("Something went wrong:", e)