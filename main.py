import asyncio
from aiogram import Bot, Dispatcher, Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart
import logging

# Initialize bot and dispatcher
bot = Bot(token="6794942349:AAFLu58hBMy-WcryXoSaSsQjsS3zTlUgmtg")
dp = Dispatcher()
rt = Router()
dp.include_router(rt)
urlGame = "https://candle.ducks-party.ru/"

@rt.callback_query(F.game_short_name == "candle")
async def get_game(
    call: CallbackQuery
):
    await call.answer(url=urlGame)

@rt.message(CommandStart())
async def get_start(
    message: Message,
    bot: Bot
):
    await message.answer_game(game_short_name="candle")

async def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - [%(levelname)s] - %(name)s - "
        "(%(filename)s).%(funcName)s(%(lineno)d) - %(message)s",
    )
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())