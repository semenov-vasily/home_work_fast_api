import fastapi
from models import Advertisement
import schema
from typing import List
from lifespan import lifespan
from depencies import SessionDependency
from crud import add_item, get_item, search_item, number_of_advertisement, search_author


app = fastapi.FastAPI(
    title="Advertisement API",
    version='0.0.1',
    description='some api',
    lifespan=lifespan
)


# Получение объявления по id с проверкой на наличие
@app.get('/v1/advertisement/{advertisement_id}/', response_model=schema.GetAdvertisementResponse)
async def get_advertisement(session: SessionDependency, advertisement_id: int):
    advertisement = await get_item(session, Advertisement, advertisement_id)
    return advertisement.dict


# Получение объявления по полю id
@app.get("/v1/advertisement_id/", response_model=schema.GetAdvertisementResponse)
async def get_adv_by_id(session: SessionDependency, advertisement_id: int):
    advertisement = await search_item(session, Advertisement, advertisement_id)
    return advertisement.dict


# Получение объявления по полю author
@app.get("/v1/advertisement_author/", response_model=List[schema.GetAdvertisementResponse])
async def get_adv_by_author(session: SessionDependency, author: str):
    total = await search_author(session, Advertisement, author)
    return [i[0].dict for i in total]


# Получение объявления по полю author через id
@app.get("/v1/advertisement_author_id/", response_model=List[schema.GetAdvertisementResponse])
async def get_adv_by_author2(session: SessionDependency, author: str):
    list_advertisement = []
    num = await number_of_advertisement(session, Advertisement, author)
    for advertisement_id in range(num + 1):
        advertisement = await search_item(session, Advertisement, advertisement_id)
        if advertisement is not None:
            advertisement = advertisement.dict
            if advertisement['author'] == author:
                list_advertisement.append(advertisement)
    return list_advertisement


# Запись нового объявления
@app.post('/v1/advertisement/', response_model=schema.CreateAdvertisementResponse,
          summary="Create new advertisement item")
async def create_advertisement(advertisement_json: schema.CreateAdvertisementRequest, session: SessionDependency):
    advertisement = Advertisement(**advertisement_json.dict())
    advertisement = await add_item(session, advertisement)
    return {'id': advertisement.id}


# Изменение объявления  по его id
@app.patch('/v1/advertisement/{advertisement_id}/', response_model=schema.UpdateAdvertisementResponse)
async def update_advertisement(advertisement_json: schema.UpdateAdvertisementRequest, session: SessionDependency,
                               advertisement_id: int):
    advertisement = await get_item(session, Advertisement, advertisement_id)
    advertisement_dict = advertisement_json.dict(exclude_unset=True)
    for field, value in advertisement_dict.items():
        setattr(advertisement, field, value)
    advertisement = await add_item(session, advertisement)
    return advertisement.dict


# Удаление объявления по его id
@app.delete('/v1/advertisement/{advertisement_id}/', response_model=schema.OkResponse)
async def delete_advertisement(advertisement_id: int, session: SessionDependency):
    advertisement = await get_item(session, Advertisement, advertisement_id)
    await session.delete(advertisement)
    await session.commit()
    return {'status': 'ok'}
