from aiogram.filters import BaseFilter
from aiogram.types import Message, CallbackQuery
from utils.utils import admin_ids


class BotAdminMessageFilter(BaseFilter):
    async def __call__(self, message: Message) -> bool:
        if flag := (message.from_user.id not in admin_ids):
            await message.reply("Вы не администратор бота")
        return not flag


class BotAdminCallbackFilter(BaseFilter):
    async def __call__(self, callback: CallbackQuery):
        if flag := (callback.from_user.id not in admin_ids):
            await callback.answer("Вы не администратор бота")
        return not flag