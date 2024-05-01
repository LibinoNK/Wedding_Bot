from aiogram.types import InputMediaPhoto
from sqlalchemy.ext.asyncio import AsyncSession

from app_wedding.database.orm_query import orm_get_banner, orm_get_season
from app_wedding.kbds.inline import get_user_main_btns, get_user_season_btns


async def main_menu(session, level, menu_name):
    banner = await orm_get_banner(session, menu_name)
    image = InputMediaPhoto(media=banner.image, caption=banner.description)

    kbds = get_user_main_btns(level=level)

    return image, kbds


async def season(session, level, menu_name):
    """ Второй уровень меню """
    banner = await orm_get_banner(session, menu_name)
    image = InputMediaPhoto(media=banner.image, caption=banner.description)

    season = await orm_get_season(session)
    kbds = get_user_season_btns(level=level, season=season)

    return image, kbds


async def get_menu_content(
        session: AsyncSession,
        menu_name: str,
        level: int,
        category: int | None = None,
        page: int | None = None,
        product_id: int | None = None,
        user_id: int | None = None,
):
    if level == 0:
        return await main_menu(session, level, menu_name)
    elif level == 10:
        return await season(session, level, menu_name)
    # elif level == 2:
    #     return await products(session, level, category, page)
    # elif level == 3:
    #     return await carts(session, level, menu_name, page, user_id, product_id)
