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

app = FastAPI()

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, log_level="info")
    
controller = Controller()

reader1 = Reader("Min", "Do")
reader2 = Reader("May", "Da")
reader3 = Reader("Moo", "Di")
reader4 = Reader("Mer", "De")
reader5 = Reader("Muc", "Du")

writer1 = Writer("write", "it")

book1 = Book("Great Book", "Fiction", 100, "intro", "Content")
book2 = Book("Thai Book", "Non-fiction", 200, "intro", "Content")
book3 = Book("Japan Book", "Non-fiction", 300, "intro", "Content")
book4 = Book("Code Book", "Non-fiction", 400, "intro", "Content")
book5 = Book("Food Book", "Non-fiction", 500, "intro", "Content")

promotion1 = Promotion("valentine", 10)
promotion2 = Promotion("new year", 15)

# book1.review.add_comment(reader1, "I really enjoyed this book!")
# book1.review.add_comment(reader2, "Highly recommend it.")
# book2.review.add_comment(reader1, "A must-read for everyone!")

# promotion1.add_book_list(book1)
# promotion1.add_book_list(book2)
# promotion2.add_book_list(book3)
# promotion2.add_book_list(book4)

controller.upload_book(book1, writer1)
controller.upload_book(book2, writer1)
controller.upload_book(book3, writer1)
controller.upload_book(book4, writer1)
controller.upload_book(book5, writer1)

controller.add_reader(reader1)
controller.add_reader(reader2)
controller.add_reader(reader3)
controller.add_reader(reader4)
controller.add_reader(reader5)

controller.add_writer(writer1)

controller.add_rating(2, 1)
controller.add_rating(2, 3)

# controller.add_promotion_list(promotion1)
# controller.add_promotion_list(promotion2)

# ------------------------------------------
# reader1.update_book_collection_list(book1)

# writer1.adding_coin = 10
# reader1.adding_coin = 2000
# ------------------------------------------

@app.get("/bookinfo", tags=['Book'])
async def get_book_info(id:int) -> dict:
    return {"Book's info": controller.show_book_info(id)}

@app.post("/transfer", tags=['money'])
async def transfer_coin_to_money(writer_id:int, data: coinInput):
    return {controller.transfer(writer_id, data.coin)}

@app.post("/rent", tags=['Cart'])
async def rent(reader_id: int, data: BookIdList):
    return {"rent": controller.rent(reader_id, data.book_id)}

@app.post("/rating", tags=['Review'])
async def add_rating(book_id: int, rating: int):
    return {"rating": controller.add_rating(book_id, rating)}