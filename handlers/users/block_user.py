from aiogram import types
from data.config import LANGUAGE_RU
from filters.filters import IsUserHasBlockMessage
from loader import dp
from utils.values import values_title


@dp.message_handler(IsUserHasBlockMessage(), state="*", content_types=types.ContentTypes.ANY)
async def block_user_message(message: types.Message):
    await message.answer(values_title.NOT_ACCESS[LANGUAGE_RU])


@dp.callback_query_handler(IsUserHasBlockMessage(), state="*")
async def block_user_callback(call: types.CallbackQuery):
    await call.answer(text=values_title.NOT_ACCESS[LANGUAGE_RU], cache_time=5, show_alert=True)


@dp.inline_handler(IsUserHasBlockMessage(), state="*")
async def block_user_inline(query: types.InlineQuery):
    await query.answer(results=[
        types.InlineQueryResultArticle(
            id="unknown",
            title=values_title.NOT_ACCESS[LANGUAGE_RU],
            input_message_content=types.InputTextMessageContent(
                message_text=values_title.NOT_ACCESS[LANGUAGE_RU],
            ),
        )
    ],
        cache_time=5)
