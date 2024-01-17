from aiogram import html
from bs4 import BeautifulSoup
import requests
import random
from time import sleep
from aiogram.types import CallbackQuery, Message
from organaizer.keyboards.inline import get_meme_keyboard, get_start_menu_keyboard
from organaizer.bot import bot as b
from organaizer.bot import start_logo
from aiogram.types import InputMediaPhoto


async def get_meme(callback: CallbackQuery):
    url = "https://www.buzzfeed.com/jamiejones/just-100-really-funny-memes-about-britain"

    def parser():
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        memes = soup.find_all("div", class_="subbuzz__media--full-width-container")
        for _ in memes:
            previous_message_id = callback.message.message_id
            return str(memes[random.randint(0, 99)].find("img")["src"]), previous_message_id

    data = parser()
    await b.edit_message_media(media=InputMediaPhoto(media=data[0]), chat_id=callback.message.chat.id,
                               message_id=data[1], reply_markup=get_meme_keyboard())
    await callback.answer()


async def back_to_menu(callback: CallbackQuery):
    await b.edit_message_media(media=InputMediaPhoto(media=start_logo,
                               caption="Вас приветствует English Bot! Выберете приложение:"),
                               chat_id=callback.message.chat.id, message_id=callback.message.message_id,
                               reply_markup=get_start_menu_keyboard())
    await callback.answer()

