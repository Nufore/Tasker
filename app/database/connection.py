from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from .db_config import DB_URL
from .models import Base


engine = create_async_engine(url=DB_URL)

async_session = async_sessionmaker(engine)


async def async_main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
