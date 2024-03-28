from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

from service.GetMessage import get_mes

router = Router()


@router.message(Command("start"))
async def start(message: Message):
    await message.answer(get_mes("main_menu_admin"))


start_rt = router
