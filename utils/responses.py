from aiogram.enums import ParseMode


# common responses
EMPTY_CATALOG = "Каталог пуст... 🤷🏻‍♂️"

# client responses
GREETING = 'Привет! Это Flower aura bot. Бот для заказа цветов.'

# admin responses
GREETING_ADMIN = 'Вы вошли в админ-панель'
ACTIONS_LIST = '''
*📝 Редактирование Списка товаров*

Добавить:\n`.add Название Цена Количество`
Пример:\n`.add Роза 117 30`

Изменить:\n`.edit ID Поле(name, price, quantity) Значение`
Пример:\n`.edit 1 price 75`

Удалить:\n`.delete ID`
Пример:\n`.delete 1`
'''
FORMAT_ERRORS = {
    "add": ("Формат: `.add Название Цена Количество`", ParseMode.MARKDOWN_V2),
    "edit": ("Формат: `.edit ID Поле Значение`", ParseMode.MARKDOWN_V2),
    "delete": ("Формат: `.delete ID`", ParseMode.MARKDOWN_V2),
}
