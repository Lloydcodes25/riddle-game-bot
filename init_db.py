import asyncio

import aiosqlite

from config import DB_PATH


async def init_db():
    async with aiosqlite.connect(DB_PATH) as conn, conn.cursor() as cur:
        await cur.execute('''CREATE TABLE IF NOT EXISTS Riddles (
                            RiddleID INTEGER PRIMARY KEY AUTOINCREMENT,
                            Riddle TEXT NOT NULL UNIQUE,
                            Answer TEXT NOT NULL
        )
        ''')
        await conn.commit()

    print(f"База данных '{DB_PATH}' создана!")
       
if __name__ == '__main__':
    asyncio.run(init_db())
