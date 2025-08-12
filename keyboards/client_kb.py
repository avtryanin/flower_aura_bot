from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def start_menu() -> InlineKeyboardMarkup:
    buttons = [
        [InlineKeyboardButton(text='Каталог 🌹', callback_data='catalog')],
        [InlineKeyboardButton(text='Корзина 🛒', callback_data='cart')]
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)


def catalog_kb() -> InlineKeyboardMarkup:
    buttons = [
        [InlineKeyboardButton(
            text='Вернуться в начало 🔙',
            callback_data='back_to_start'
        )]
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)
