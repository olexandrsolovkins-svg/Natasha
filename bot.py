import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from config import TELEGRAM_TOKEN
from natasha_ai import ask_natasha

bot = Bot(token=TELEGRAM_TOKEN)
dp = Dispatcher()

@dp.message()
async def handle_message(message: Message):
    reply = await ask_natasha(message.text)
    await message.answer(reply)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
