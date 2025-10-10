import asyncio
import os
from aiogram import Bot, Dispatcher
from app.database.DB import setup_database, db
from app.handlers import router
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_BOT_API = os.environ.get("TELEGRAM_BOT_API")
bot = Bot(token=TELEGRAM_BOT_API)
dp = Dispatcher()


async def main():
    if not setup_database():
        print("setup database error in run.py")
        return False
    dp.include_router(router)
    if not db:
        print("database service is unavailable")
        return False
    dp.workflow_data["db"] = db  # нужна ли эта хуйня

    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("exit")
