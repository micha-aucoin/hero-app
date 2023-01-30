from typing import Optional
from datetime import datetime

from sqlalchemy import Column, event
from sqlalchemy.databases import postgres
from sqlmodel import Field, SQLModel

from app.core.models import TimestampModel, UUIDModel
from app.quotes.examples import ex_quotes_create, ex_quotes_read


class QuotesBase(SQLModel):
    date: datetime = Field(index=True)
    Open: float
    High: float
    Low: float
    Close: float
    Volume: Optional[int] = Field(default=None, index=True)
    Dividends: Optional[float] = Field(default=None, index=True)


class Quotes(TimestampModel, QuotesBase, UUIDModel, table=True):
    pass


class QuotesRead(QuotesBase, UUIDModel):
    class Config:
        schema_extra = {"example": ex_quotes_read}


class QuotesCreate(QuotesBase):
    class Config:
        schema_extra = {"example": ex_quotes_create}