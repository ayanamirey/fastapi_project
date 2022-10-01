from typing import List
from datetime import date
from pydantic import BaseModel, validator


class Genre(BaseModel):
    name: str


class Author(BaseModel):
    first_name: str
    last_name: str
    age: int

    @validator('age')
    def check_age(cls, v):
        if v < 15:
            raise ValueError('Возраст автора не может быть меньше 15')
        return v


class Book(BaseModel):
    title: str
    writer: str
    duration: str
    date: date
    summary: str
    genres: List[Genre]
    pages: int
