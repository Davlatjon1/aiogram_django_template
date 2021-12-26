from aiogram import Dispatcher

from loader import dp
from .filters import IsUserHasBlockMessage


if __name__ == "filters":
    dp.filters_factory.bind(IsUserHasBlockMessage)

