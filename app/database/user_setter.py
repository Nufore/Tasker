from sqlalchemy import select
from .connection import async_session
from .models import Users


async def set_user(tg_id: int):
    async with async_session() as session:
        stmt = select(Users).where(Users.tg_id == tg_id)
        user = await session.scalar(stmt)

        if not user:
            new_user = Users(tg_id=tg_id)
            session.add(new_user)
            await session.commit()
