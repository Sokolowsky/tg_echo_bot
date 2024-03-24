from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message

BOT_TOKEN = 'blablabla'
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

#Handler for /start
async def process_start_command(message: Message):
    await message.answer('Привет!\nМеня зовут Эхо-бот!\nНапиши мне что-нибудь')

#Handler for /help
async def process_help_command(message: Message):
    await message.answer(
        'Напиши мне что-нибудь и в ответ '
        'я пришлю тебе твое сообщение')
async def process_photo_command(message: Message):
    await message.answer_photo(message.photo[-1].file_id)

async def process_sticker_command(message: Message):
    await message.answer_sticker(message.sticker.file_id)

async def process_voice_command(message: Message):
    await message.answer_voice(message.voice.file_id)

async def send_echo(message: Message):
    await message.answer(text=message.text)

dp.message.register(process_start_command, Command(commands='start'))
dp.message.register(process_help_command, Command(commands='help'))
dp.message.register(process_photo_command, F.photo)
dp.message.register(process_sticker_command, F.sticker)
dp.message.register(process_voice_command, F.voice)
dp.message.register(send_echo)

if __name__ == '__main__':
    dp.run_polling(bot)
