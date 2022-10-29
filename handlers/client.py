from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from Keyboards.client_kb import start_markup
from parser.hdz import parser

from config import dp, bot

# @dp.message_handler(commands=['start', 'help'])
async def start_handler(message:types.Message):
    await bot.send_message(message.from_user.id, f'Добро пожаловать в Страх и Отвращение в GeekTech, {message.from_user.first_name}')

# @dp.message_handler(commands=['quiz'])
async def quiz_1(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton("next", callback_data='button_call_1')
    markup.add(button_call_1)
    question = 'Кто такие битники?'
    answers = [
        "хиппари",
        "разбитое поколение",
        "наркоши",
        "писатели",
        "мне почем"
    ]
    await bot.send_poll(
        chat_id=message.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=1,
        explanation='нам нельзя тут оставаться',
        reply_markup=markup


    )

# @dp.message_handler(commands=['meme'])
async def meme_bot(message: types.Message):
  photo = open('test/' + random.choice(os.listdir('test')), 'rb')
  await bot.send_photo(message.from_user.id, photo)

async def parser_series(message: types.Message):
    items = parser()
    for item in items:
        await message.answer(
            f"{item['link']}\n\n"
            f"{item['title']}\n"
            f"{item['year']}\n"
            f"{item['country']}\n"
            f"{item['genre']}\n"
        )

def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(start_handler, commands=['start', 'help'])
    dp.register_message_handler(quiz_1, commands=['quiz'])
    dp.register_message_handler(meme_bot, commands=['meme'])
    dp.register_message_handler(parser_series, commands=['series'])
