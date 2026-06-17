from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from dotenv import load_dotenv
import asyncio
import os

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(TOKEN)
dp = Dispatcher()

menu = ReplyKeyboardMarkup(
keyboard=[
[KeyboardButton(text="💵 Продажа")],
[KeyboardButton(text="👥 Клиенты")],
[KeyboardButton(text="📊 Отчет")]
],
resize_keyboard=True
)

@dp.message(Command("start"))
async def start(message: Message):
    await message.answer(
        "👋 Добро пожаловать в BOTKASSA",
        reply_markup=menu
    )

@dp.message()
async def handler(message: Message):

    if message.text=="💵 Продажа":
        await message.answer(
            "Введите сумму продажи"
        )

if __name__=="__main__":
    asyncio.run(dp.start_polling(bot))
