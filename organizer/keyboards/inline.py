from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram import types


def finance_keyboard():
    keyboard_builder = InlineKeyboardBuilder()

    keyboard_builder.button(text="Установить баланс", callback_data="set_balance")
    keyboard_builder.button(text="Редактировать баланс", callback_data="edit_balance")
    return keyboard_builder.as_markup(resized_keyboard=True)


def get_balance_editor_keyboard():
    keyboard_builder = InlineKeyboardBuilder()

    keyboard_builder.button(text="Доход", callback_data="edit_balance"),
    keyboard_builder.button(text="Расход", callback_data="edit_balance"),
    return keyboard_builder.as_markup(resized_keyboard=True)
