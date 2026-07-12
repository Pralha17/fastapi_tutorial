from fastapi import FastAPI, status
from fastapi.exceptions import HTTPException
from pydantic import BaseModel

app = FastAPI()
books = [
    {"id": 1,
     "title": "The Great Gatsby",
     "author": "F. Scott Fitzgerald",
     "published_year": 1925},
    {"id":2,
     "title": "To Kill a Mockingbird",
     "author": "Harper Lee",
     "published_year": 1960},
    {"id":3,
     "title": "1984",
     "author": "George Orwell",
     "published_year": 1949},
     {"id":4,
     "title": "Pride and Prejudice",
     "author": "Jane Austen",
     "published_year": 1813},

]

app = FastAPI()

@app.get("/books")
def get_books():
    return books

@app.get("/books/{book_id}")
def get_book(book_id:int):
    for book in books:
        if book['id'] == book_id:
            return book
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail = "Book not found")


class Book(BaseModel):
    id:int
    title:str
    author:str
    published_year:int  

@app.post("/books")
def create_book(book: Book):
    new_book = book.model_dump()
    books.append(new_book)
    return new_book

class BookUpdate(BaseModel):
    title:str
    author:str
    published_year:int

@app.put("/books/book_id")
def update_book(book_id:int, book_update: BookUpdate):
    for book in books:
        if book['id'] == book_id:
            book['title'] = book_update.title
            book['author'] = book_update.author
            book['published_year'] = book_update.published_year
            return book
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Book not found")

@app.delete("/books/{book_id}")
def delete_book(book_id:int):
    for book in books:
        if book['id'] == book_id:
            books.remove(book)
            return {"message": "Book deleted successfully!!"}
    
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")