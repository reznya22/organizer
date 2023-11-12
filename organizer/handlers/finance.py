from aiogram import types
from keyboards.inline import get_balance_editor_keyboard, finance_keyboard
from utils.callbackdata import UserFinance


async def show_balance(message: types.Message):
    await message.answer(f"Ваш баланс {UserFinance.balance}$",
                         reply_markup=finance_keyboard())


async def set_balance(callback: types.CallbackQuery):
    await callback.message.answer(f"В разработке")
    await callback.answer()


async def edit_balance(callback: types.CallbackQuery):
    await callback.message.answer(f"В разработке",
                                  reply_markup=get_balance_editor_keyboard())
    await callback.answer()
