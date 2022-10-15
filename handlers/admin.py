from aiogram import types, Dispatcher
from configg import dp, bot
from random import choice

async def pin_bot(message: types.Message):
    if message.text.reply_to_message:
        await bot.pin_chat_message(message.chat.id, message.message_id)
    else:
        print('сообщение должно быть ответом')
    emoj = ['⚽', '🏀', '🥅', '🎲', '🎯', '🎰', '🎳']
    if message.text == 'game':
        await bot.send_dice((message.chat.id,emoj))
def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(pin_bot, commands=['pin'])