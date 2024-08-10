import datetime
from typing import Literal
from pydantic import BaseModel


class OkResponse(BaseModel):
    status: Literal['ok']


class GetAdvertisementResponse(BaseModel):
    id: int
    name: str
    description: str
    price: int
    author: str
    date_of_creation: datetime.datetime


class CreateAdvertisementRequest(BaseModel):
    name: str
    description: str
    price: int
    author: str


class CreateAdvertisementResponse(BaseModel):
    id: int


class UpdateAdvertisementRequest(BaseModel):
    name: str | None = None
    description: str | None = None
    price: int | None = None
    author: str | None = None


class UpdateAdvertisementResponse(CreateAdvertisementResponse):
    pass
