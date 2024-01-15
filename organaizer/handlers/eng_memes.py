from aiogram import html
from aiogram.types import CallbackQuery, Message
from organaizer.keyboards.inline import get_meme_keyboard


async def get_meme(callback: CallbackQuery):
    await callback.answer()

