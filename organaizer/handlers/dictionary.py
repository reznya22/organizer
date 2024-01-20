from aiogram.types import CallbackQuery, Message, InputMediaPhoto
from organaizer.keyboards.inline import get_dictionary_keyboard
from organaizer.media.media import *
from dotenv import load_dotenv
import organaizer.main
import psycopg2
import os


async def get_dictionary(callback: CallbackQuery):
    if callback.message.content_type == "photo":
        await organaizer.main.bot.edit_message_media(media=InputMediaPhoto(media=dict_opened_logo,
                                                     caption="Enter words like  < *eng word : ru word* > ",
                                                     parse_mode="Markdown"),
                                                     chat_id=callback.message.chat.id,
                                                     message_id=callback.message.message_id)
    else:
        await organaizer.main.bot.send_photo(chat_id=callback.message.chat.id,
                                             photo=dict_opened_logo,
                                             caption="Enter words like  < *eng word : ru word* > ",
                                             parse_mode="Markdown",
                                             reply_markup=get_dictionary_keyboard())
    await callback.answer()


async def add_word_to_db(message: Message):
    try:
        load_dotenv()

        conn = psycopg2.connect(dbname=os.getenv("DBNAME"), user=os.getenv("DBUSER"),
                                password=os.getenv("PASSWORD"), host=os.getenv("HOST"))
        conn.autocommit = True

        with conn.cursor() as curs:
            curs.execute("""SELECT user_id FROM users_info WHERE user_id = %s;""",
                         (message.from_user.id,))

            if not curs.fetchone():  # if user already in db this step is skipped

                curs.execute("""
                                INSERT INTO users_info (user_id, username)
                                VALUES (%s, %s);
                                """,
                             (message.from_user.id, message.from_user.username))

            curs.execute("""
                                SELECT eng_word 
                                FROM users 
                                WHERE eng_word = %s AND user_id = %s;
                                """,
                         (message.text.split(" : ")[0], message.from_user.id))

            if not curs.fetchone():  # if eng word not already in db word added to db

                curs.execute("""
                                INSERT INTO users (user_id, eng_word, ru_word)
                                VALUES (%s, %s, %s);
                                """,
                             (message.from_user.id, message.text.split(" : ")[0], message.text.split(" : ")[1]))

                await organaizer.main.bot.send_photo(message.chat.id,
                                                     caption="*Words are successfully added to dictionary*",
                                                     parse_mode="Markdown",
                                                     reply_markup=get_dictionary_keyboard(),
                                                     photo=dict_closed_logo)
            else:  # if eng word not already in db word added to db
                curs.execute("""
                                   SELECT eng_word, ru_word 
                                   FROM users 
                                   WHERE eng_word = %s AND user_id = %s;
                                   """,
                             (message.text.split(" : ")[0], message.from_user.id))
                await organaizer.main.bot.send_photo(message.chat.id,
                                                     caption="Message is already in a dictionary:\n" +
                                                             f"*{' : '.join(curs.fetchone())}*",
                                                     parse_mode="Markdown",
                                                     reply_markup=get_dictionary_keyboard(),
                                                     photo=dict_closed_logo)

    except:
        await message.answer("*Sorry something was wrong =(*",
                             parse_mode="Markdown",
                             reply_markup=get_dictionary_keyboard())


async def back_to_menu(callback: CallbackQuery):
    message = callback.message
    await organaizer.main.start(message)

    await callback.answer()
