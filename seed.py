import asyncio

import aiosqlite

from config import DB_PATH
from riddles_data import get_riddles_dict


async def seed_riddles():
    async with aiosqlite.connect(DB_PATH) as conn, conn.cursor() as cur:
        for riddle, answer in get_riddles_dict().items():
            await cur.execute(
                'INSERT OR IGNORE INTO Riddles (Riddle, Answer) VALUES (?, ?)',
                (riddle, answer)
            )
        await conn.commit()
    print("Загадки добавлены (без дублей.)")
    
if __name__ == "__main__":
    asyncio.run(seed_riddles())