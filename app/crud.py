from sqlalchemy import Select, func, select, desc
from models import Session, Advertisement
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException
import typing


# Запись объявления в бд с проверкой
async def add_item(session: Session, item: Advertisement):
    session.add(item)
    try:
        await session.commit()
    except IntegrityError as err:
        if err.orig.pgcode == "23505":
            raise HTTPException(status_code=409, detail='Item already exist')
        raise err
    return item


# Получение записи из бд по id с проверкой на наличие
async def get_item(session: Session, orm_cls: typing.Type[Advertisement], item_id: int):
    orm_object = await session.get(orm_cls, item_id)
    if orm_object is None:
        raise HTTPException(status_code=404,
                            detail=f'{orm_cls.__name__} not found')
    return orm_object


# Получение записи из бд по id без проверки
async def search_item(session: Session, orm_cls: typing.Type[Advertisement], item_id: int):
    orm_object = await session.get(orm_cls, item_id)
    return orm_object


# Получение всех записей из бд по автору
async def search_author(session: Session, orm_cls: typing.Type[Advertisement], author: str):
    total = await session.execute(select(orm_cls).where(orm_cls.author == author))
    return total


# Получение максимального id из записей в бд по автору
async def number_of_advertisement(session: Session, orm_cls: typing.Type[Advertisement], author: str):
    last_advertisement = await session.execute(
        select(orm_cls).where(orm_cls.author == author).order_by(orm_cls.id.desc()).limit(1))
    num = int(next(last_advertisement)[0].dict['id'])
    return num
