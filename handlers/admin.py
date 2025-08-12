from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.enums import ParseMode
from sqlalchemy.exc import SQLAlchemyError

from database import crud
from utils.logger import logger, log_action
from keyboards.admin_kb import start_admin
from utils.formatters import format_products
from utils.responses import (
    GREETING_ADMIN,
    EMPTY_CATALOG,
    ACTIONS_LIST,
    FORMAT_ERRORS
)
from utils.validators import (
    require_admin,
    parse_add_command,
    parse_edit_command,
    parse_delete_command
)


router = Router()


@router.message(F.text == '/admin')
@require_admin
async def admin_panel(message: Message):
    await message.answer(GREETING_ADMIN, reply_markup=start_admin())
    log_action('Admin', message.from_user, " opened admin-panel")


@router.callback_query(F.data == 'product_list')
@require_admin
async def product_list(callback: CallbackQuery, session):
    products = await crud.get_all_products(session)
    text = format_products(products, show_quantity=True) or EMPTY_CATALOG
    await callback.message.edit_text(text, reply_markup=start_admin())
    await callback.answer()
    log_action('Admin', callback.from_user, "got product list")


@router.callback_query(F.data == 'actions')
@require_admin
async def actions(callback: CallbackQuery):
    await callback.message.edit_text(
        text=ACTIONS_LIST,
        parse_mode=ParseMode.MARKDOWN_V2,
        reply_markup=start_admin()
    )
    await callback.answer()
    log_action('Admin', callback.from_user, "opened actions list")


@router.message(F.text.startswith('.add '))
@require_admin
async def add_product(message: Message, session):
    try:
        name, price, quantity = parse_add_command(message.text)
        await crud.create_product(session, name, price, quantity)
        await message.answer('Товар добавлен!')
    except (ValueError, TypeError):
        text, mode = FORMAT_ERRORS["add"]
        await message.answer(text=text, parse_mode=mode)
    except SQLAlchemyError as e:
        logger.error(f"Database error in add_product: {e}")
    except Exception as e:
        logger.error(f"Unexpected error in add_product: {e}")


@router.message(F.text.startswith('.delete '))
@require_admin
async def delete_product(message: Message, session):
    try:
        pid = parse_delete_command(message.text)
        await crud.delete_product(session, pid)
        await message.answer('Товар удален.')
    except (ValueError, TypeError):
        text, mode = FORMAT_ERRORS["delete"]
        await message.answer(text=text, parse_mode=mode)
    except SQLAlchemyError as e:
        logger.error(f"Database error in delete_product: {e}")
    except Exception as e:
        logger.error(f"Unexpected error in delete_product: {e}")


@router.message(F.text.startswith('.edit '))
@require_admin
async def edit_product(message: Message, session):
    try:
        pid, field, value = parse_edit_command(message.text)
        await crud.update_product(session, pid, **{field: value})
        await message.answer('Товар обновлен.')
    except (ValueError, TypeError):
        text, mode = FORMAT_ERRORS["edit"]
        await message.answer(text=text, parse_mode=mode)
    except SQLAlchemyError as e:
        logger.error(f"Database error in edit_product: {e}")
    except Exception as e:
        logger.error(f"Unexpected error in edit_product: {e}")
