from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from dotenv import load_dotenv
import asyncio
import os

load_dotenv()

bot = Bot(os.getenv("BOT_TOKEN"))
dp = Dispatcher()

sales = {}

menu = ReplyKeyboardMarkup(
keyboard=[
[KeyboardButton(text="💵 Продажа")],
[KeyboardButton(text="📊 Отчет")],
[KeyboardButton(text="👥 Клиенты")]
],
resize_keyboard=True
)

waiting_sale = set()

@dp.message(Command("start"))
async def start(message: Message):

    await message.answer(
        "👋 Добро пожаловать в BOTKASSA",
        reply_markup=menu
    )

@dp.message()
async def messages(message: Message):

    user = message.from_user.id

    if message.text == "💵 Продажа":
        waiting_sale.add(user)

        await message.answer(
            "Введите сумму продажи:"
        )
        return

    if user in waiting_sale:

        try:
            amount = int(message.text)

            sales[user] = sales.get(
                user,
                0
            ) + amount

            waiting_sale.remove(user)

            await message.answer(
                f"✅ Продажа {amount:,} сум сохранена"
            )

        except:
            await message.answer(
                "Введите число"
            )

    elif message.text == "📊 Отчет":

        total = sales.get(
            user,
            0
        )

        await message.answer(
            f"📈 Общая выручка:\n{total:,} сум"
        )

if __name__ == "__main__":
    asyncio.run(
        dp.start_polling(bot)
    )
