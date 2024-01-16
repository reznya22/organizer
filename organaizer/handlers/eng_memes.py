from aiogram import html
from bs4 import BeautifulSoup
import requests
import random
from time import sleep
from aiogram.types import CallbackQuery, Message
from organaizer.keyboards.inline import get_meme_keyboard, get_start_menu_keyboard
from organaizer import bot


async def get_meme(callback: CallbackQuery):
    url = "https://www.buzzfeed.com/jamiejones/just-100-really-funny-memes-about-britain"

    def parser():
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        memes = soup.find_all("div", class_="subbuzz__media--full-width-container")
        for _ in memes:
            return str(memes[random.randint(0, 100)].find("img")["src"])

    await callback.message.answer(parser(), reply_markup=get_meme_keyboard())

    await callback.answer()

