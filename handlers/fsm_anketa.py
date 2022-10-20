from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram .dispatcher.filters.state import State, StatesGroup
from config import bot
from random import choice
from Keyboards.client_kb import gender_markup, submit_markup, cancel_markup

mentor_ids = []

class FSMAdmin(StatesGroup):
    photo = State()
    name = State()
    age = State()
    direction = State()
    group = State()
    gender = State()
async def fsm_start(message: types.Message):
    if message.chat.type == 'private':
        await FSMAdmin.photo.set()
        await message.answer(
            f'здравствуй {message.from_user.full_name} '
            f'отправьте фотографию, желательно качественную и не уродливую'
        )
    else:
        await message.answer('в личку надо дебил')
async def load_photo(message: types.Message, state: FSMContext):
    chislo = choice(range(1, 100000))
    while chislo in mentor_ids:
        chislo = choice(range(1, 100000))
    mentor_ids.append(chislo)
    async with state.proxy() as data:
        data['id'] = chislo
        data['username'] = f'@{message.from_user.username}'
        data['photo'] = message.photo[0].file_id
        await FSMAdmin.next()
        await message.answer('я вот бот, а вот кто ты?')

async def load_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
        await FSMAdmin.next()
        await message.answer('сколько лет?')

async def load_age(message: types.Message, state: FSMContext):
    try:
        if not 15 < int(message.text) < 50:
            await message.answer('ты либо старенький либо глупенький')
            await state.finish()
            return
        async with state.proxy() as data:
            data['age'] = int(message.text)
        await FSMAdmin.next()
        await message.answer('направление?')
    except:
        await message.answer('Пиши числа!')


async def load_direction(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['direction'] = message.text
        await FSMAdmin.next()
        await message.answer('группa?')

async def load_group(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['group'] = message.text
        await FSMAdmin.next()
        await message.answer('какой твой пол?')

async def load_gender(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['gender'] = message.text
        await bot.send_photo(message.from_user.id, data['photo'],
                             caption=f"{data['name']}, {data['age']}, {data['gender']} "
                                     f"{data['region']}\n\n{data['username']}")
    await FSMAdmin.next()
    await message.answer('верно?!', reply_markup=submit_markup)

async def submit(message: types.Message, state: FSMContext):
    if message.text.lower() == "да":

        await state.finish()
        await message.answer('Регистрация завершена')
    if message.text.lower() == 'нет':
        await state.finish()
        await message.answer('Отменено')
    else:
        await message.answer('чтоо')



async def cancel_reg(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is not None:
        await state.finish()
        await message.answer('Отменено')


def register_handlers_fsm_anketa(dp:Dispatcher):
    dp.register_message_handler(cancel_reg, state='*', commands=['cancel'])
    dp.register_message_handler(cancel_reg, Text(equals='cancel', ignore_case=True),
                                state='*')
    dp.register_message_handler(fsm_start, commands=['anket'])
    dp.register_message_handler(load_photo, state=FSMAdmin.photo, content_types=['photo'])
    dp.register_message_handler(load_name, state=FSMAdmin.name)
    dp.register_message_handler(load_age, state=FSMAdmin.age)
    dp.register_message_handler(load_direction, state=FSMAdmin.direction)
    dp.register_message_handler(load_group, state=FSMAdmin.group)
    dp.register_message_handler(load_gender, state=FSMAdmin.gender)
    dp.register_message_handler(submit, state=FSMAdmin.submit)

