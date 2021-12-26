from aiogram import types
from aiogram.dispatcher.filters import BoundFilter
from utils.db_api import db_commands


class IsUserHasBlockMessage(BoundFilter):
    async def check(self, message: types.Message) -> bool:
        user = await db_commands.get_user(user_id=message.from_user.id,
                                          full_name=message.from_user.full_name,
                                          username=message.from_user.username)
        return not user.access
