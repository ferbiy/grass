import asyncio
import sys
from pathlib import Path

# Add the project root to Python path
sys.path.append(str(Path(__file__).parent))

from core.utils.accounts_db import AccountsDB
from data.config import PROXY_DB_PATH

async def cleanup():
    db = AccountsDB(PROXY_DB_PATH)
    await db.connect()
    
    try:
        await db.clean_unused_proxies()
    except Exception as e:
        print(f"Error cleaning database: {e}")
    finally:
        await db.close_connection()

if __name__ == "__main__":
    asyncio.run(cleanup()) 