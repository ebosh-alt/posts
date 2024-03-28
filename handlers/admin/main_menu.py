from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from data.config import bot
from filters import Filters
from service.GetMessage import get_mes

router = Router()


@router.message(Filters.IsAdmin(), Command("admin"))
async def main_menu(message: Message):
    user_id = message.from_user.id
    await bot.send_message(chat_id=user_id,
                           text=get_mes("main_menu_admin"))

main_menu_rt = router
