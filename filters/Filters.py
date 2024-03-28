from aiogram.filters import Filter
from aiogram.types import Message, User

from data.config import admins


# from bot.config import admin_id
# from bot.data import users

class IsAdmin(Filter):
    async def __call__(self, message: Message, event_from_user: User) -> bool:
        if event_from_user.id in admins:
            return True
        return False
