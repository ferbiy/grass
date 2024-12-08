import asyncio
from core.utils.accounts_db import AccountsDB
from data.config import PROXY_DB_PATH

async def cleanup():
    db = AccountsDB(PROXY_DB_PATH)
    await db.connect()
    await db.clean_all_proxy_data()
    await db.close_connection()
    print("Database cleaned successfully")

if __name__ == "__main__":
    asyncio.run(cleanup()) 