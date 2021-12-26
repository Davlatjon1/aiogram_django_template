from aiogram import executor
import django
import os
from utils.set_bot_commands import set_default_commands


async def on_startup(dispatcher):
    import middlewares, filters, handlers

    from utils.notify_admins import on_startup_notify

    # Устанавливаем дефолтные команды
    await set_default_commands(dispatcher)

    # Уведомляет про запуск
    await on_startup_notify(dispatcher)


def setup_django():
    os.environ.setdefault(
        "DJANGO_SETTINGS_MODULE",
        "django_project.telegrambot.telegrambot.settings"
    )
    os.environ.update({'DJANGO_ALLOW_ASYNC_UNSAFE': "true"})
    django.setup()


if __name__ == '__main__':
    setup_django()

    from aiogram import executor
    from loader import dp

    executor.start_polling(dp, on_startup=on_startup)
