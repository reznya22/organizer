from aiogram import types
from keyboards.reply import get_note_keyboard


async def notes_list(message: types.Message):
    await message.answer("<b>Ваши заметки:\n</b>",
                         reply_markup=get_note_keyboard())


# @dp.callback_query(F.data == "add_note")
async def add_note(callback: types.CallbackQuery):
    await callback.message.answer("Введите новую заметку:")


