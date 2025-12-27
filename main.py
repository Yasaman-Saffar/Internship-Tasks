import asyncio
from aiogram import Dispatcher, Bot
from config import BOT_TOKEN
from handlers import routers

async def main():
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()
    
    for router in routers:
        dp.include_router(router)
        
    print('Bot is running...')
    await dp.start_polling(bot)
    
if __name__ == "__main__":
    asyncio.run(main())