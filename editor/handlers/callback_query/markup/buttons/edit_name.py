from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext

from editor.cbdata import ButtonCallbackData


async def edit_name(
        callback_query: CallbackQuery,
        callback_data: ButtonCallbackData,
        state: FSMContext
):
    pass
