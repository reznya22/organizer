from organaizer.keyboards.inline import get_meme_keyboard
from aiogram.types import InputMediaPhoto
from aiogram.types import CallbackQuery
from bs4 import BeautifulSoup
import organaizer.main
import requests
import random


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
    await organaizer.main.bot.edit_message_media(media=InputMediaPhoto(media=data[0]),
                                                 chat_id=callback.message.chat.id,
                                                 message_id=data[1],
                                                 reply_markup=get_meme_keyboard())
    await callback.answer()


async def back_to_menu(callback: CallbackQuery):
    message = callback.message
    await organaizer.main.start(message)

    await callback.answer()

