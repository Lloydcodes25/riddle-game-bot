import asyncio

from aiogram import Bot, Dispatcher, F, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove

from config import BOT_TOKEN
from game_logic import check_answer, get_random_riddle

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()
ATTEMPTS = 4

class RiddleState(StatesGroup):
    waiting_for_answer = State()
    
keyboard = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text='Загадку?')],],
    resize_keyboard=True,
    one_time_keyboard=False
)

@dp.message(Command("start"))
async def start_cmd(message: types.Message):
    await message.answer("Добро пожаловать!", reply_markup=keyboard)
     
@dp.message(F.text == "Загадку?")
async def what_will_do_next(message: types.Message, state: FSMContext):
    if message.text == 'Загадку?':
        riddle, correct_answer = await get_random_riddle()
        if riddle is None:
            await message.answer("Загадки закончились")
            return
    
        await state.update_data(
            correct_answer=correct_answer,
            attempts=0,
            )
        
        await state.set_state(RiddleState.waiting_for_answer)
        
        await message.answer(f"Угадай загадку:\n\n{riddle}", reply_markup=ReplyKeyboardRemove()) 
    else:
        await message.answer('Что то пошло не так!')
  
@dp.message(RiddleState.waiting_for_answer)
async def check_riddle(message: types.Message, state: FSMContext):
    data = await state.get_data()
    correct_answer = data.get("correct_answer")
    attempts = data.get("attempts", 0)
    
    if correct_answer is None:
        await message.answer("Что-то пошло не так. Начни заново: /start")
        return
    
    user_answer = check_answer(message.text)
    
    if user_answer == correct_answer:
        await message.answer(f"\n'{correct_answer}'. Молодец!", reply_markup=keyboard)
        await state.clear()
        return
    
    attempts += 1
    
    if attempts >= ATTEMPTS:
        await message.answer(
            f"\nПравильным ответом на загадку будет '{correct_answer}'.",
            reply_markup=keyboard,
        )
        await state.clear()
        return
    
    await state.update_data(attempts=attempts)
    await message.answer(
        f"\nПопытка {attempts}: Нет, не '{message.text}'. Старайтесь лучше."
    )

async def main():
    print("Бот запущен и работает...")
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())