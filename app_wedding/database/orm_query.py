import math
from sqlalchemy import select, update, delete
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload

from app_wedding.database.models import Banner, User, Season


# from database.models import Banner, Cart, Category, Product, User

############### Работа с баннерами (информационными страницами) через админку ###############

async def orm_add_banner_description(session: AsyncSession, data: dict):
    # Добавляем новый или изменяем существующий по именам
    # пунктов меню: main, season, amount, place, style, colors, fashion, costume, end
    query = select(Banner)
    result = await session.execute(query)
    if result.first():
        return
    session.add_all([Banner(name=name, description=description) for name, description in data.items()])
    await session.commit()


async def orm_change_banner_image(session: AsyncSession, name: str, image: str):
    query = update(Banner).where(Banner.name == name).values(image=image)
    await session.execute(query)
    await session.commit()


async def orm_get_banner(session: AsyncSession, page: str):
    query = select(Banner).where(Banner.name == page)
    result = await session.execute(query)
    return result.scalar()


async def orm_get_info_pages(session: AsyncSession):
    query = select(Banner)
    result = await session.execute(query)
    return result.scalars().all()


##################### Добавляем юзера в БД #####################################

async def orm_add_user(
        session: AsyncSession,
        user_id: int,
        first_name: str | None = None,
):
    query = select(User).where(User.user_id == user_id)
    result = await session.execute(query)
    if result.first() is None:
        session.add(
            User(user_id=user_id, first_name=first_name)
        )
        await session.commit()

############################ Сезоны ######################################

async def orm_get_season(session: AsyncSession):
    query = select(Season)
    result = await session.execute(query)
    return result.scalars().all()

async def orm_create_season(session: AsyncSession, season: list):
    query = select(Season)
    result = await session.execute(query)
    if result.first():
        return
    session.add_all([Season(name=name) for name in season])
    await session.commit()