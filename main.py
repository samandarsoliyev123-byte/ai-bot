import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

BOT_TOKEN = "8670422076:AAHCaW7uCBd14kjDVbmrS7kddTVAxUYM3Sw"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start_handler(message: types.Message):
    await message.answer("Salom! Men AI botman")

@dp.message()
async def ai_handler(message: types.Message):
    await message.answer(f"Siz yozdingiz: {message.text}")

async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())# ai-bot
