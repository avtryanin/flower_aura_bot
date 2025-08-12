from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from contextlib import asynccontextmanager

from config import DATABASE_URL


Base = declarative_base()

engine = create_async_engine(DATABASE_URL, echo=True)
async_session_maker = sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False
)


@asynccontextmanager
async def get_session():
    async with async_session_maker() as session:
        yield session
