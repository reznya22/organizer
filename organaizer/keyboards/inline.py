from aiogram.utils.keyboard import InlineKeyboardBuilder


def get_start_menu_keyboard():
    keyboard_builder = InlineKeyboardBuilder()

    keyboard_builder.button(text="Dictionary", callback_data="get_dictionary")
    keyboard_builder.button(text="Skill test", callback_data="start_skill_test")
    keyboard_builder.button(text="Random text", callback_data="get_random_text")
    keyboard_builder.button(text="Random meme", callback_data="get_random_meme")

    keyboard_builder.adjust(2, 2)

    return keyboard_builder.as_markup()


def get_meme_keyboard():  # parsing, beautifulsoup
    keyboard_builder = InlineKeyboardBuilder()

    keyboard_builder.button(text="Back to menu", callback_data="back_to_menu_from_eng_memes")
    keyboard_builder.button(text="Get random meme", callback_data="get_random_meme")

    return keyboard_builder.as_markup()


def get_skill_test_keyboard():
    pass


def get_random_text_keyboard():  # parsing, beautifulsoup
    pass


def get_dictionary_keyboard():  # Database, Postgres, read, update and delete
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text="Add word", callback_data="add_word")
    keyboard_builder.button(text="Back to menu", callback_data="back_to_menu_from_dict")  # add all words view button

    return keyboard_builder.as_markup()

