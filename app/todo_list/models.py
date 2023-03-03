from typing import Optional

from sqlalchemy import UniqueConstraint
from sqlmodel import Field, SQLModel

from app.core.models import TimestampModel, UUIDModel
from app.heroes.examples import ex_hero_create, ex_hero_patch, ex_hero_read

prefix = "hrs"


class UserBase(SQLModel):
    email: str = Field(max_length=255, nullable=False, index=True)
    name: str = Field(max_length=255, nullable=False, index=True)
    username: str = Field(max_length=255, nullable=False, index=True)
    hashed_password: str = Field(max_length=255, nullable=False)


    


class User(
    TimestampModel,
    UserBase,
    UUIDModel,
    table=True,
):
    _table_args__ = (
        UniqueConstraint("email"),
        UniqueConstraint("username"),
    )





class HeroRead(UserBase, UUIDModel):
    class Config:
        schema_extra = {"example": ex_hero_read}


class HeroCreate(UserBase):
    class Config:
        schema_extra = {"example": ex_hero_create}


class HeroPatch(UserBase):
    nickname: Optional[str] = Field(max_length=255)

    class Config:
        schema_extra = {"example": ex_hero_patch}



class Task(SQLModel):
    test: str = Field(nullable=False, index=True)