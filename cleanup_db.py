import asyncio
from core.utils.accounts_db import AccountsDB
from core.utils import logger
from data.config import PROXY_DB_PATH

async def cleanup():
    db = AccountsDB(PROXY_DB_PATH)
    await db.connect()
    
    try:
        await db.clean_unused_proxies()
    except Exception as e:
        logger.error(f"Error cleaning database: {e}")
    finally:
        await db.close_connection()

if __name__ == "__main__":
    asyncio.run(cleanup()) 