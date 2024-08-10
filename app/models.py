import datetime
from config import PG_DSN
from sqlalchemy import Integer, DateTime, String, func, Text
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine

engine = create_async_engine(PG_DSN,)

Session = async_sessionmaker(bind=engine, expire_on_commit=False)


class Base(AsyncAttrs, DeclarativeBase):
    pass


class Advertisement(Base):
    __tablename__ = 'advertisement'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(200), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=False)
    price: Mapped[int] = mapped_column(Integer, nullable=False)
    author: Mapped[str] = mapped_column(String, nullable=False)
    date_of_creation: Mapped[datetime.datetime] = mapped_column(
        DateTime,
        server_default=func.now()
    )

    @property
    def dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'price': self.price,
            'author': self.author,
            'date_of_creation': self.date_of_creation.isoformat()
        }
