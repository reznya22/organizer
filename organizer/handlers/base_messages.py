from aiogram import types
from aiogram import html


async def hello(message: types.Message):
    await message.answer(f"Hi, {html.bold(html.italic(message.from_user.full_name))}")
