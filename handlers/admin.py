from aiogram import types, Dispatcher
from config import dp, bot
from random import choice

async def pin_bot(message: types.Message):
    if message.text.reply_to_message:
        await bot.pin_chat_message(message.chat.id, message.message_id)
    else:
        print('сообщение должно быть ответом')
async def game_bot(message: types.Message):
    azart = ['⚽', '🏀', '🥅', '🎲', '🎯', '🎰', '🎳']
    await bot.send_dice(message.chat.id, emoji='azart')
def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(pin_bot, commands=['pin'])
    dp.register_message_handler(game_bot, commands=['game'])
