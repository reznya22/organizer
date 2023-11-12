import asyncio
import logging
from aiogram import F
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from utils.commands import set_commands
from config_reader import config
from handlers import notes, base_messages, finance, plans
from keyboards.reply import start_keyboard


async def start(message: types.Message, bot: Bot):
    await set_commands(bot)
    await message.answer(
        "<b>Выберете приложение:</b>", reply_markup=start_keyboard)


async def main():
    # Включаем логирование, чтобы не пропустить важные сообщения
    logging.basicConfig(level=logging.INFO)

    bot = Bot(token=config.bot_token.get_secret_value(), parse_mode="HTML")
    dp = Dispatcher()

    dp.message.register(start, Command(commands=["run", "start"]))
    dp.message.register(notes.notes_list, F.text.lower() == "заметки")
    dp.callback_query.register(notes.add_note, F.data == "add_note")
    dp.message.register(base_messages.hello, F.text.lower() == "hi")
    dp.message.register(finance.show_balance, F.text.lower() == "финансы")
    dp.callback_query.register(finance.edit_balance, F.data == "edit_balance")
    dp.callback_query.register(finance.set_balance, F.data == "set_balance")

    # Запуск процесса поллинга новых апдейтов
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
