import asyncio
from contextlib import suppress
import logging

from config import dp, bot
from handlers import routers


# from handlers import routers
# from bot.config import bot, dp


async def main() -> None:
    for router in routers:
        dp.include_router(router)

    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        filemode="w",
                        format="%(levelname)s %(asctime)s %(message)s",
                        encoding='utf-8')

    with suppress(KeyboardInterrupt):
        asyncio.run(main())
