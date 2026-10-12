"""
Модуль для работы с загадками.
Содержит функции получения случайной загадки и проверки ответов.
"""

import aiosqlite

from config import DB_PATH


async def get_random_riddle():
    async with aiosqlite.connect(DB_PATH) as conn, conn.cursor() as cur:
        await cur.execute('SELECT Riddle, Answer FROM Riddles ORDER BY RANDOM() LIMIT 1')  
        row = await cur.fetchone()
    if row is None:
        return None, None # или raise
    riddle = row[0]; correct_answer = row[1]
    return riddle, correct_answer

def check_answer(answer): 
    """Привести к нужной форме введенный пользователем ответ."""
    answer = answer.lower().strip()
    symbols = [',', '.', '?', '!', '@', '#', '$', '%', '^', '&', '*',
    '/', '\\', '|', '~', '`', '-', '+', '=', '"', "'", '№', ';', ':',
    '(', ')', '()', '<', '>',]
    for symbol in symbols:
        answer = answer.replace(symbol, '') if symbol in answer else answer
    
    return answer