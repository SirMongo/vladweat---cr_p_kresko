from aiogram.utils import executor

from telegram.tg_bot_interface import dp


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
