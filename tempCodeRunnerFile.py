o", tags=['Book'])
# async def get_book_info(id:int) -> dict:
#     return {"Book's info": controller.show_book_info(id)}

# @app.post("/transfer", tags=['money'])
# async def transfer_coin_to_money(writer_id:int, data: coinInput):
#     return {controller.transfer(writer_id, data.coin)}

# @app.post("/rent", tags=['Cart'])
# async def rent(reader_id: int, data: BookIdList):
#     return {"rent": controller.rent(reader_id, data.book_id)}

# @app.get("/bookfrompromotion", tags=['Book'])
# async def get_book_by_promotion(promotion:str) -> dict:
#     return {"Book in this promotion": controller.search_book_by_promotion(promotion)}

# @app.post("/rating", tags=['Review'])
# async def add_rating(book_id: int, rating: int):
#     return {"rating": controller.add_rating(book_id, rating)}