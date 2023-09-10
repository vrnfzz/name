import logging

from aiogram import Bot, Dispatcher, executor, types

from environs import Env
env = Env()
env.read_env()
TOKEN = env.str('BOT_TOKEN')

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def echo(message: types.Message):
    await message.reply('Start')

@dp.message_handler(commands=['help'])
async def echo1(message: types.Message):
    await message.reply('Вы обратились к справке бота')

@dp.message_handler(content_types=types.ContentType.TEXT)
async def hello(message: types.Message):
    text = message.text.lower()
    if text == 'привет':
        await message.reply('Привет')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)