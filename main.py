from typing import Optional
from typing import Union
from typing import List
from fastapi import FastAPI
from BaseModel_class import coinInput, BookIdList
import uvicorn
import os
from Controller_class import Controller
from Account_class import Reader, Writer
from Book_class import Book
from Review_class import Review
from Promotion_class import Promotion

# app = FastAPI()

# if __name__ == "__main__":
#     uvicorn.run("main:app", host="127.0.0.1", port=8000, log_level="info")
    
controller = Controller()

book1 = Book("Great Book", 1, "writer1", "Fiction", 100, "intro", "Content")
book2 = Book("Thai Book", 2, "writer1", "Non-fiction", 200, "intro", "Content")
book3 = Book("Japan Book", 3, "writer1", "Non-fiction", 300, "intro", "Content")
book4 = Book("Code Book", 4, "writer1", "Non-fiction", 400, "intro", "Content")
book5 = Book("Food Book", 5, "writer1", "Non-fiction", 500, "intro", "Content")

reader1 = Reader("John", "Doe", 1)
reader2 = Reader("May", "Da", 2)
reader3 = Reader("May", "Da", 3)
reader4 = Reader("May", "Da", 4)
reader5 = Reader("May", "Da", 5)

writer1 = Writer("write", "it", 1)

promotion1 = Promotion("valentine", 10)
promotion2 = Promotion("new year", 15)

book1.review = Review(reader1, book1, "2024-02-28 10:00:00")
book2.review = Review(reader2, book2, '0')

book1.review.add_comment(reader1, "I really enjoyed this book!")
book1.review.add_comment(reader2, "Highly recommend it.")
book2.review.add_comment(reader1, "A must-read for everyone!")
book1.review.add_rating(5)
book2.review.add_rating(4)

promotion1.add_book_list(book1)
promotion1.add_book_list(book2)
promotion2.add_book_list(book3)
promotion2.add_book_list(book4)

controller.add_book(book1)
controller.add_book(book2)
controller.add_book(book3)
controller.add_book(book4)
controller.add_book(book5)

controller.add_reader(reader1)
controller.add_reader(reader2)
controller.add_reader(reader3)
controller.add_reader(reader4)
controller.add_reader(reader5)

controller.add_writer(writer1)

controller.add_promotion_list(promotion1)
controller.add_promotion_list(promotion2)

reader1.update_book_collection_list(book1)

writer1.adding_coin = 10
reader1.adding_coin = 2000

# @app.get("/bookinfo", tags=['Book'])
# async def get_book_info(id:int) -> dict:
#     return {"Book's info": controller.show_book_info(id)}

# @app.post("/transfer", tags=['money'])
# async def transfer_coin_to_money(writer_id:int, data: coinInput):
#     return {controller.transfer(writer_id, data.coin)}

# @app.post("/rent", tags=['Cart'])
# async def rent(reader_id: int, data: BookIdList):
#     return {"rent": controller.rent(reader_id, data.book_id)}