from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import AsyncEngine
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlmodel import SQLModel
from src.config import Config

async_engine = AsyncEngine(create_engine(url=Config.DATABASE_URL, echo=False))


async def init_db():
    async with async_engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)


async def get_session() -> AsyncSession:
    Session = sessionmaker(bind=async_engine, class_=AsyncSession, expire_on_commit=False)
    async with Session() as session:
        yield session






