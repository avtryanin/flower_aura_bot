from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def start_admin() -> InlineKeyboardMarkup:
    buttons = [
        [InlineKeyboardButton(
            text='Список товаров 📜',
            callback_data='product_list'
        )],
        [InlineKeyboardButton(
            text='Действия ✍🏼',
            callback_data='actions'
        )]
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)
