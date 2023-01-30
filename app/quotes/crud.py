from typing import List
from uuid import UUID

import yfinance as yf
from fastapi import HTTPException
from fastapi import status as http_status
from sqlalchemy import delete, select
from sqlmodel.ext.asyncio.session import AsyncSession

from app.quotes.models import Quotes, QuotesCreate


class QuotesCRUDY:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, data: QuotesCreate) -> Quotes:
        values = data.dict()

        quotes = Quotes(**values)
        self.session.add(quotes)
        await self.session.commit()
        await self.session.refresh(quotes)

        return quotes

    async def yf_quoted_hist(self, ticker: str, period: str):  # -> List[Quotes]
        tik = yf.Ticker(ticker=ticker)
        if tik == None:
            raise HTTPException(
                status_code=http_status.HTTP_404_NOT_FOUND,
                detail="The ticker can't been found!",
            )
        hist = tik.history(period=period)

        hist.index.name = "date"
        hist.reset_index(inplace=True)

        # quotes = Quotes(*[f"**{x}" for x in hist.to_dict(orient="records")])

        return hist.to_dict(orient="records")