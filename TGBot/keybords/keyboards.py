from aiogram import types

button1 = types.KeyboardButton(text='/start')
button2 = types.KeyboardButton(text='Стоп')
button3 = types.KeyboardButton(text='Инфо')
button4 = types.KeyboardButton(text='Хз')
button5 = types.KeyboardButton(text='фото')

keyboard1 = [
    [button1, button2, button3, button4 , button5]
]
keyboard2 = [
    [button3, button2, button1, button5 , button4]
]
keyboard3 = [
    [button5, button4, button3, button2 , button1]
]
kb1 = types.ReplyKeyboardMarkup(keyboard=keyboard1,resize_keyboard=True)
kb2 = types.ReplyKeyboardMarkup(keyboard=keyboard2,resize_keyboard=True)
kb3 = types.ReplyKeyboardMarkup(keyboard=keyboard3,resize_keyboard=True)