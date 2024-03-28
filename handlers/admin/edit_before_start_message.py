import logging

from aiogram import Router, F
from aiogram.types import CallbackQuery

from data.config import bot
from service.GetMessage import get_mes
from service import keyboards as kb
from models import BeforeStartMessage

router = Router()
logger = logging.getLogger(__name__)


@router.callback_query(F.data == "Редактирование предстартового сообщения")
async def start_edit_before_start_message(message: CallbackQuery):
    id = message.from_user.id
    await bot.send_message(chat_id=id,
                           text=get_mes("start_edit_before_start_message.md"),
                           reply_markup=kb.edit_before_start_message_kb)


@router.callback_query(F.data.in_(kb.edit_before_start_message_button))
async def action_edit_before_start_message(message: CallbackQuery):
    logger.info(f"start edit before start-message: {message.data}")
    match message.data:
        case "Изменить видимость":
            await change_visibility(message)
        case "Медиа":
            await view_media(message)
        case "Клавиатура":
            ...


async def view_media(message: CallbackQuery):
    user_id = message.from_user.id
    bsm = BeforeStartMessage()  # before start message - bsm
    media = bsm.get_media()
    buttons = []
    for el in media:
        buttons.append(el.name)
    await bot.send_message(chat_id=user_id,
                           text="Существующие на данный момент медиа-файлы",
                           reply_markup=kb.create_keyboard(buttons))
    logger.info("Successfully view media")


async def change_visibility(message: CallbackQuery):
    bsm = BeforeStartMessage()  # before start message - bsm
    bsm.active = not bsm.active
    if bsm.active:
        await bot.answer_callback_query(callback_query_id=message.id, text="Блок виден")
    else:
        await bot.answer_callback_query(callback_query_id=message.id, text="Блок не виден")


edit_before_start_message_rt = router
