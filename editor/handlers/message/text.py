from aiogram import Bot
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from ...utils.send_message import send_message
from ...utils.send_panel import send_panel
from ...enums import MediaPosition


async def text(
        message: Message,
        state: FSMContext,
        bot: Bot
):
    await state.update_data({
        "text": message.html_text,
        "markup": message.reply_markup.model_dump_json() if message.reply_markup else None,
        "disable_web_page_preview": True,
        "has_spoiler": message.has_media_spoiler,
        "media_position": MediaPosition.UP
    })

    chat_id = message.chat.id

    await send_message(
        chat_id=chat_id,
        state=state,
        bot=bot
    )

    await send_panel(
        chat_id=chat_id,
        state=state,
        bot=bot
    )
