from fastapi import FastAPI
from data_processing import library_data, Book

library = library_data("library.json")

books: list[Book] = library.books

app = FastAPI()


@app.get("/books")
async def read_books():
    return books

# path parameter
@app.get("/book/{id}")
async def read_book_by_id(id: int):
    return [book for book in books if book.id == id][0]


@app.post("/books/create_book")
async def create_book(book_request: Book):
    ...
