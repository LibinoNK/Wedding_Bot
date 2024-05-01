from aiogram.filters.callback_data import CallbackData
from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


class MenuCallBack(CallbackData, prefix="menu"):
    menu_name: str
    level: int
    season: str | None = None
    # image_id: int | None = None


def get_user_main_btns(*, level: int, sizes: tuple[int] = (2,)):
    keyboard = InlineKeyboardBuilder()
    btns = {
        "Старт квиза 🍕": "quiz",
        "Результат 🛒": "result",
        "О боте ℹ️": "about_b",
        "О нас 💰": "about",
    }
    for text, menu_name in btns.items():
        if menu_name == 'quiz':
            keyboard.add(InlineKeyboardButton(text=text,
                                              callback_data=MenuCallBack(level=10, menu_name='quiz').pack()))
        elif menu_name == 'result':
            keyboard.add(InlineKeyboardButton(text=text,
                                              callback_data=MenuCallBack(level=1, menu_name=menu_name).pack()))
        else:
            keyboard.add(InlineKeyboardButton(text=text,
                                              callback_data=MenuCallBack(level=level, menu_name=menu_name).pack()))

    return keyboard.adjust(*sizes).as_markup()


def get_user_season_btns(*, level: int, sizes: tuple[int] = (2,)):
    keyboard = InlineKeyboardBuilder()
    btns = {
        "Старт квиза 🍕": "quiz",
        "Результат 🛒": "result",
        "О боте ℹ️": "about_b",
        "О нас 💰": "about",
    }
    for text, menu_name in btns.items():
        if menu_name == 'quiz':
            keyboard.add(InlineKeyboardButton(text=text,
                                              callback_data=MenuCallBack(level=10, menu_name='quiz').pack()))
        elif menu_name == 'result':
            keyboard.add(InlineKeyboardButton(text=text,
                                              callback_data=MenuCallBack(level=1, menu_name=menu_name).pack()))
        else:
            keyboard.add(InlineKeyboardButton(text=text,
                                              callback_data=MenuCallBack(level=level, menu_name=menu_name).pack()))

    return keyboard.adjust(*sizes).as_markup()

# def get_user_season_btns(*, level: int, season: list, sizes: tuple[int] = (2,)):
#     keyboard = InlineKeyboardBuilder()
#
#     keyboard.add(InlineKeyboardButton(text='Весна',
#                                       callback_data=MenuCallBack(level=3, menu_name='spring').pack()))
#     keyboard.add(InlineKeyboardButton(text='Зима',
#                                       callback_data=MenuCallBack(level=3, menu_name='winter').pack()))
#     keyboard.add(InlineKeyboardButton(text='Лето',
#                                       callback_data=MenuCallBack(level=3, menu_name='summer').pack()))
#     keyboard.add(InlineKeyboardButton(text='Осень',
#                                       callback_data=MenuCallBack(level=3, menu_name='autumn').pack()))
#     keyboard.add(InlineKeyboardButton(text='Назад',
#                                       callback_data=MenuCallBack(level=0, menu_name='main').pack()))
#
#     for c in season:
#         keyboard.add(InlineKeyboardButton(text=c.name,
#                                           callback_data=MenuCallBack(level=20, menu_name=c.name,
#                                                                      category=c.id).pack()))
#
#     return keyboard.adjust(*sizes).as_markup()

# def get_user_season_btns(*, level: int, sizes: tuple[int] = (2,)):
#     """ Инлайн билдер клавиатуры со словарем ключ значение"""
#     keyboard = InlineKeyboardBuilder()
#     btns = {
#         "Осень": "autumn",
#         "Зима": "winter",
#         "Весна": "spring",
#         "Лето": "summer",
#     }
#     for text, menu_name in btns.items():
#         if menu_name == 'autumn':
#             keyboard.add(InlineKeyboardButton(text=text,
#                                               callback_data=MenuCallBack(level=11, menu_name=menu_name).pack()))
#         elif menu_name == 'winter':
#             keyboard.add(InlineKeyboardButton(text=text,
#                                               callback_data=MenuCallBack(level=12, menu_name=menu_name).pack()))
#         elif menu_name == 'spring':
#             keyboard.add(InlineKeyboardButton(text=text,
#                                               callback_data=MenuCallBack(level=13, menu_name=menu_name).pack()))
#         elif menu_name == 'summer':
#             keyboard.add(InlineKeyboardButton(text=text,
#                                               callback_data=MenuCallBack(level=14, menu_name=menu_name).pack()))
#
#
#     return keyboard.adjust(*sizes).as_markup()
