from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_async_session
from app.quotes.crud import QuotesCRUD


async def get_quotes_crud(
    session: AsyncSession = Depends(get_async_session),
) -> QuotesCRUD:
    return QuotesCRUD(session=session)