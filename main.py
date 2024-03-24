from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message

BOT_TOKEN = 'paste here'

#Bot and dispatcher classes
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

#/Start handler
@dp.message(Command(commands='start'))
async def process_start_command(message: Message):
    await message.answer('Привет, я тупой слаборазвитый бот, который все что умеет, это повторять!')

#/Help handler
@dp.message(Command(commands='help'))
async def process_help_command(message: Message):
    await message.answer('Напиши мне что-нибудь!')

#Handler for everything expect help/start
@dp.message()
async def send_echo(message: Message):
    try:
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.reply(text='Я ваще не пойму че это')

if __name__ == '__main__':
    dp.run_polling(bot)
