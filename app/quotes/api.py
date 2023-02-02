from typing import List
from fastapi import APIRouter, Depends
from fastapi import status as http_status

from app.core.models import StatusMessage
from app.quotes.crud import QuotesCRUD
from app.quotes.dependencies import get_quotes_crud
from app.quotes.models import QuotesCreate, QuotesRead

router = APIRouter()


@router.post(
    "",
    response_model=QuotesRead,
    status_code=http_status.HTTP_201_CREATED,
)
async def create_quoted_hist(
    data: QuotesCreate,
    qt: QuotesCRUD = Depends(get_quotes_crud),
):
    quotes = await qt.create(data=data)

    return quotes


# @router.get(
#     "/{ticker}/history",
#     # response_model=List[QuotesRead],
#     status_code=http_status.HTTP_200_OK,
# )
# async def search_yfinance(
#     *,
#     ticker: str,
#     period: str,
#     qt: QuotesCRUD = Depends(get_quotes_crud),
# ):
#     quote = await qt.yf_quoted_hist(ticker=ticker, period=period)

#     return quote