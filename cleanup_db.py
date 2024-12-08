import asyncio
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent))

from core.utils.accounts_db import AccountsDB
from data.config import PROXY_DB_PATH

async def cleanup_associations():
    db = AccountsDB(PROXY_DB_PATH)
    await db.connect()
    
    try:
        async with db.db_lock:
            # Get current accounts before cleanup
            await db.cursor.execute("SELECT email FROM Accounts")
            accounts = await db.cursor.fetchall()
            
            # Clear proxy associations
            await db.cursor.execute("UPDATE Accounts SET proxies = ''")
            await db.delete_all_from_extra_proxies()
            await db.connection.commit()
            
            print(f"Successfully cleared proxy associations for {len(accounts)} accounts")
    except Exception as e:
        print(f"Error during cleanup: {e}")
    finally:
        await db.close_connection()

if __name__ == "__main__":
    asyncio.run(cleanup_associations()) 