from handlers import eng_memes, dictionary, skill_test, texts_for_reading
from keyboards.inline import get_start_menu_keyboard
from organaizer.media.media import start_logo
from aiogram.filters.command import Command
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from dotenv import load_dotenv
import asyncio
import logging
import os


load_dotenv()
bot = Bot(token=os.getenv("BOT_TOKEN"), parse_mode="HTML")


async def main():
    logging.basicConfig(level=logging.INFO)

    dp = Dispatcher()

    dp.message.register(start, Command(commands=["start"]))
    dp.callback_query.register(eng_memes.get_meme, F.data == "get_random_meme")
    dp.callback_query.register(eng_memes.back_to_menu, F.data == "back_to_menu_from_eng_memes")
    dp.callback_query.register(dictionary.get_dictionary, F.data == "get_dictionary")
    dp.callback_query.register(dictionary.back_to_menu, F.data == "back_to_menu_from_dict")
    dp.callback_query.register(dictionary.get_dictionary, F.data == "add_word")
    dp.message.register(dictionary.add_word_to_db)

    await dp.start_polling(bot)


async def start(message: Message, keyboard=get_start_menu_keyboard):
    await bot.send_photo(
        chat_id=message.chat.id,
        photo=start_logo,
        reply_markup=keyboard(),
        caption="Hello it's a *English Bot*! Select any application:",
        parse_mode="Markdown",
    )


if __name__ == "__main__":
    asyncio.run(main())
