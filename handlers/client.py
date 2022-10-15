from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from configg import dp, bot

# @dp.message_handler(commands=['start', 'help'])
async def start_handler(message:types.Message):
    await bot.send_message(message.from_user.id, f'Добро Пожаловать в Культ Пелевина, {message.from_user.first_name}')

# @dp.message_handler(commands=['quiz'])
async def quiz_1(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton("next", callback_data='button_call_1')
    markup.add(button_call_1)
    question = 'Причем тут Че Ге Вара?'
    answers = [
        "при всем",
        "не причем",
        "зачем",
        "Мухомор",
        "Краска"
    ]
    await bot.send_poll(
        chat_id=message.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,
        explanation='о отче наш',
        reply_markup=markup


    )

# @dp.message_handler(commands=['meme'])
async def meme_bot(message: types.Message):
  photo = open('test/' + random.choice(os.listdir('test')), 'rb')
  await bot.send_photo(message.from_user.id, photo)

def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(start_handler, commands=['start', 'help'])
    dp.register_message_handler(quiz_1, commands=['quiz'])
    dp.register_message_handler(meme_bot, commands=['meme'])
