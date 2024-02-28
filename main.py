from typing import Optional
from typing import Union
from fastapi import FastAPI
import uvicorn
from Controller_class import Controller
from Account_class import Reader
from Account_class import Writer
from Book_class import Book
from Review_class import Review
from Promotion_class import Promotion

app = FastAPI()

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, log_level="info")
    
controller = Controller()

reader1 = Reader("John", "Doe", "1")
reader2 = Reader("May", "Da", "2")
writer1 = Writer("write", "it", "1")
book = Book("Great Book", 1, writer1, "Fiction", 100, "intro", "Content")
book.review = Review(reader1, book, "2024-02-28 10:00:00")
book.review = Review(reader2, book, '0')

book.review.add_comment(reader1, "I really enjoyed this book!")
book.review.add_comment(reader2, "Highly recommend it.")
book.review.add_comment(reader1, "A must-read for everyone!")
book.review.add_rating(5)
book.review.add_rating(4)

book.promotion = Promotion("valentine", 10, book)

controller.add_book(book)
controller.add_reader(reader1)
controller.add_reader(reader2)
controller.add_writer(writer1)

@app.get("/bookinfo", tags=['Book'])
async def get_book_info(id:int) -> dict:
    return {"Book's info": controller.show_book_info(id)}