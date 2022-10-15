from aiogram import types, Dispatcher
from configg import dp, bot


# @dp.message_handler()
async def echo(message: types.Message):
    if message.text.isdigit():
        k = int(message.text)
        await bot.send_message(message.chat.id, k * k)
    else:
        await bot.send_message(message.from_user.id, message.text)

def register_handlers_extra(dp:Dispatcher):
    dp.register_message_handler(echo)