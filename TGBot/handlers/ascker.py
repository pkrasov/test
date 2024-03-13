
import keybords.keyboards as keyboards
import keybords.dynamicboard as dnkb
import webreq as req
from aiogram import F,types,Router
from aiogram.filters.command import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State,StatesGroup

dp = Router()

list_first = ["Выбор 1","Выбор 2","Выбор 3"]
list_second = ["Выбор 4","Выбор 5","Выбор 6"]

class StatusSteps(StatesGroup):
    stepNames = State()
    stepGrades = State()

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
@dp.message(Command('ask'))
async def cmd_ask(message: types.Message,state: FSMContext):
    await message.answer('Опрос 1',reply_markup=dnkb.get_dynamic_kb(list_first))
    await state.set_state(StatusSteps.stepNames)

@dp.message(StatusSteps.stepNames,F.text)
async def cmd_ask12(message: types.Message,state: FSMContext):
    if((list_first.__contains__(message.text))):
        await state.update_data(first_choise=message.text.lower())
        await message.answer('Опрос 2',reply_markup=dnkb.get_dynamic_kb(list_second))
        await state.set_state(StatusSteps.stepGrades)
    else:
        await message.answer('Опрос 1',reply_markup=dnkb.get_dynamic_kb(list_first))

@dp.message(StatusSteps.stepGrades,F.text)
async def cmd_ask22(message: types.Message,state: FSMContext):
    if((list_second.__contains__(message.text))):
        await state.update_data(second_choise=message.text.lower())
        await state.set_state(StatusSteps.stepNames)
        ud = await state.get_data() 
        await message.answer(f'Вы выбрали опрос1 {ud.get("first_choise")} и опрос2 {ud.get("second_choise")}',reply_markup=types.ReplyKeyboardRemove())    
    else:
        await message.answer('Опрос 2',reply_markup=dnkb.get_dynamic_kb(list_second))