
import keybords.keyboards as keyboards
import webreq as req
from aiogram import F,types,Router
from aiogram.filters.command import Command
import logging
import random

dp = Router()

@dp.message(Command('start'))
async def cmd_start(message: types.Message):
    name = message.chat.first_name
    print(message)
    await message.answer(f'Салют {name} используй /keys')

@dp.message(Command('keys'))
async def cmd_info(message: types.Message):
    name = message.chat.first_name
    print(message)
    
    await message.answer(f'Вот что можно', reply_markup=keyboards.kb1)  

@dp.message(F.text)
async def cmd_info(message: types.Message):

   # print(message)
    if message.text=='фото':
   #   ft = req.getphoto()
      await message.answer_photo(photo=req.getphoto())
     # await bot.send_photo(photo=req.getphoto(),chat_id=message.from_user.id)    
    await message.answer(f'фильтр {message.text}',reply_markup=types.ReplyKeyboardRemove())    

