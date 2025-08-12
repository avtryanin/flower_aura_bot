from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command

from database import crud
from utils.logger import log_action
from keyboards.client_kb import (
    start_menu,
    catalog_kb
)
from utils.formatters import format_products
from utils.responses import (
    GREETING,
    EMPTY_CATALOG
)

router = Router()


@router.message(Command('start'))
async def cmd_start(message: Message):
    await message.answer(GREETING, reply_markup=start_menu())
    log_action('User', message.from_user, "started bot")


@router.callback_query(F.data == 'back_to_start')
async def back_to_start(callback: CallbackQuery):
    await callback.message.edit_text(GREETING, reply_markup=start_menu())
    await callback.answer()
    log_action('User', callback.from_user, "returned to start menu")


@router.callback_query(F.data == 'catalog')
async def catalog(callback: CallbackQuery, session):
    products = await crud.get_all_products(session)
    text = format_products(products) or EMPTY_CATALOG
    await callback.message.edit_text(text, reply_markup=catalog_kb())
    await callback.answer()
    log_action('User', callback.from_user, "opened catalog")
