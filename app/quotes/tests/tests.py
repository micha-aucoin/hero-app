import pytest
from httpx import AsyncClient
from fastapi import status as http_status
from fastapi.encoders import jsonable_encoder
from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.quotes.models import Quotes


@pytest.mark.asyncio
async def test_create_quoted_hist(
    async_client: AsyncClient,
    async_session: AsyncSession,
    test_data: dict,
):
    """Store historical quotes in a SQL database"""

    payload = test_data["case_create"]["payload"]
    response = await async_client.post(
        "/quotes",
        json=payload,
    )

    assert response.status_code == http_status.HTTP_201_CREATED

    got = response.json()
    want = test_data["case_create"]["want"]

    for k, v in want.items():
        assert got[k] == v

    statement = select(Quotes).where(Quotes.uuid == got["uuid"])
    results = await async_session.execute(statement=statement)
    und = jsonable_encoder(results.scalar_one())

    for k, v in want.items():
        assert und[k] == v


@pytest.mark.asyncio
async def test_search_yfinance(
    async_client: AsyncClient,
    async_session: AsyncSession,
    test_data: dict,
):
    ticker = "spy"
    period = "5d"
    response = await async_client.get(
        f"/quotes/{ticker}/history?period={period}"
    )

    assert response.status_code == http_status.HTTP_200_OK

    """ callback """