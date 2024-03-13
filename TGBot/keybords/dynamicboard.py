from aiogram import types

def get_dynamic_kb(items: list[str]) ->types.ReplyKeyboardMarkup:
    row = [types.KeyboardButton(text=item) for item in items]
    return types.ReplyKeyboardMarkup(keyboard=[row],resize_keyboard=True)
