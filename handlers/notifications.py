import aioschedule
from aiogram import types, Dispatcher
from config import bot
import asyncio
import os

async def get_chat_id(message: types.Message):
    global chat_id
    chat_id = message.from_user.id
    await message.answer("Got it!")

async def read_vagabond():
    await bot.send_message(chat_id=chat_id, text='please read vagabond, its fcking masterpiece')

async def work_out():
    photo = open('power/Valkyricons.jpg')
    await bot.send_photo(chat_id=chat_id, photo=photo)
    await bot.send_message(chat_id=chat_id, text='WORKOUT!')

async def scheduler():
    aioschedule.every().friday.at('16:30').do(read_vagabond)
    aioschedule.every().tuesday.at('17:40').do(work_out)
    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(5)

def register_handlers_notification(dp: Dispatcher):
    dp.register_message_handler(get_chat_id,
                                lambda word: 'напомни' in word.text)