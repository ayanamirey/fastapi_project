from fastapi import FastAPI, Query, Path, Body
from fastapi.params import Body

from schemas import Book, BookOut
from typing import List

app = FastAPI()


#
# @app.get('/')
# def home():
#     return {'key': 'hello'}
#
#
# @app.get('/{pk}')
# def get_item(pk: int, q: str = None):
#     return {'key': pk, 'q': q}
#
#
# @app.get('/user/{pk}/items/{item}/')
# def get_user_item(pk: int, item: str):
#     return {'user': pk, 'item': item}
#
#
# @app.post('/book', response_model=Book, response_model_include={'date', 'pages'})
# def create_book(item: Book):
#     return {'item': item}
#
#
# @app.get('/book/')
# def get_book(q: List[str] = Query(..., description='Search book')):
#     return q
#
#
# @app.get('/book/{pk}')
# def get_single_book(pk: int = Path(..., gt=1, le=20), pages: int = Query(None, gt=10, le=500)):
#     return {'pk': pk, 'pages': pages}
#
#
# @app.post('/author/')
# def create_author(author: Author = Body(..., embed=True)):
#     return {'author': author}

@app.post('/book', response_model=BookOut)
def create_book(item: Book):
    book = item.dict()
    book['id'] = 5
    return book
    # return BookOut(**item.dict(), id=3)
