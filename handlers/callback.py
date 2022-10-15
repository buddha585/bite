from aiogram import types,  Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from configg import dp, bot

# @dp.callback_query_handler(lambda call: call.data == 'button_call_1')
async def quiz_2(message: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton("next thing you do is press this button", callback_data='button_call_2')
    markup.add(button_call_1)
    question = 'В чем отличие неформального подростка в 21-м веке и некрофила?'
    answers = [
        "гнилость",
        "нету, оба являются анархистами",
        "никаких",
        "много отличий"
    ]
    await bot.send_poll(
        chat_id=message.from_user.id,
        question=question,
        options=answers,\

        is_anonymous=False,
        type='quiz',
        correct_option_id=1,
        explanation='ты черт подери прав',
        reply_markup = markup


    )

# @dp.callback_query_handler(lambda call: call.data == 'button_call_1')
async def quiz_2(message: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton("next thing you do is press this button", callback_data='button_call_2')
    markup.add(button_call_1)
    question = 'В чем отличие неформального подростка в 21-м веке и некрофила?'
    answers = [
        "гнилость",
        "нету, оба являются анархистами",
        "никаких",
        "много отличий"
    ]
    await bot.send_poll(
        chat_id=message.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=1,
        explanation='ты черт подери прав',
        reply_markup = markup


    )
# @dp.callback_query_handler(lambda call: call.data == 'button_call_2')
async def quiz_3(message: types.CallbackQuery):
    question = 'в каком году распался СССР'
    answers = [
        "1979",
        "1985",
        "1987",
        "1989",
        "1991"
    ]
    await bot.send_poll(
        chat_id=message.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=4,
        explanation="растрелять",


    )


def register_handlers_callback(dp: Dispatcher):
    dp.register_callback_query_handler(quiz_2, lambda call: call.data=='button_call_1')
    dp.register_callback_query_handler(quiz_3, lambda call: call.data == 'button_call_2')
