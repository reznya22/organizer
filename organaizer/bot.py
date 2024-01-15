import asyncio
import logging
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.filters.command import Command
from config_reader import config
from handlers import eng_memes, dictionary, skill_test, texts_for_reading
from keyboards.inline import get_start_menu_keyboard

bot = Bot(token=config.bot_token.get_secret_value(), parse_mode="HTML")


async def main():
    logging.basicConfig(level=logging.INFO)

    dp = Dispatcher()

    dp.message.register(start, Command(commands=["start"]))
    dp.callback_query.register(eng_memes.get_meme, F.data == "get_random_meme")

    await dp.start_polling(bot)


async def start(message: Message, keyboard=get_start_menu_keyboard):
    await bot.send_photo(
        message.chat.id,
        photo="https://en.wikipedia.org/wiki/Flag_of_the_United_Kingdom#/media/File:Flag_of_the_United_Kingdom_(1-2).svg",
        reply_markup=keyboard(),
        caption="Вас приветствует English Bot! Выберете приложение:",
    )


if __name__ == "__main__":
    asyncio.run(main())
