from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder

start_keyboard = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text="Заметки"),
        KeyboardButton(text="Планы"),
        KeyboardButton(text="Финансы")
    ],
    [
        KeyboardButton(text="В разработке"),
        KeyboardButton(text="В разработке"),
        KeyboardButton(text="В разработке")
    ]
], resize_keyboard=True, one_time_keyboard=True,
   input_field_placeholder="Выберете приложение↓")


def get_note_keyboard():
    keyboard_builder = ReplyKeyboardBuilder()

    keyboard_builder.button(text="Добавить заметку"),
    keyboard_builder.button(text="Редактировать"),
    keyboard_builder.button(text="На главную")

    keyboard_builder.adjust(2, 1)
    return keyboard_builder.as_markup(resize_keyboard=True, one_time_keyboard=False,
                                      inpu_filed_placeholer="Выберете действие↓")

