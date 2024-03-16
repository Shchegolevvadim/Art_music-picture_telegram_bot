from aiogram import Bot, Dispatcher, F, types
import asyncio
from utils.commands import set_commands
from aiogram.types import Message, CallbackQuery

bot = Bot(token="6997573174:AAFleF0x1uru7e_vYdnS2xkAsy_zUpjgKZU", parse_mode='HTML')
dp = Dispatcher()
admin_id = "1121648600"

async def start_bot( bot: Bot):
    await bot.send_message(admin_id, f"Здравствуйте, рады приветствовать вас на нашем боте на котором вы сможете просмотреть фотографии различных направлений !")
dp.startup.register(start_bot)

async def start():
    await set_commands(bot)
    try:
        await dp.start_polling(bot, skip_updates=True)
    finally:
        await bot.session.close()

if __name__ == '__main__':
    asyncio.run(start())
