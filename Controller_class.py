import datetime
from Review_class import Review

class Controller:
    def __init__(self):
        self.__reader_list = []
        self.__writer_list = []
        self.__complain_list = []
        self.__book_list = []
        self.__payment_method_list = []
        self.__promotion_list = []
        self.__num_of_book = 0
        self.__num_of_account = 0

    @property
    def reader_list(self):
        return self.__reader_list
    
    @property
    def writer_list(self):
        return self.__writer_list

    @property
    def complain_list(self):
        return self.__complain_list

    @property
    def book_list(self):
        return self.__book_list

    @property
    def payment_method_list(self):
        return self.__payment_method_list
    
    @property
    def promotion_list(self):
        return self.__promotion_list

    def add_reader(self, reader):
        self.__num_of_account += 1
        reader.id_account = self.__num_of_account
        self.__reader_list.append(reader)
        
    def add_writer(self, writer):
        self.__num_of_account += 1
        writer.id_account = self.__num_of_account
        self.__writer_list.append(writer)

    def add_complain(self, complain):
        self.__complain_list.append(complain)

    def upload_book(self, book, writer):
        self.__num_of_book += 1
        book.id = self.__num_of_book
        self.__book_list.append(book)
        writer.book_collection_list.append(book)

    def add_payment_method(self, payment_method):
        self.__payment_method_list.append(payment_method)
        
    def add_promotion_list(self, promotion):
        self.__promotion_list.append(promotion)
        for prom in self.__promotion_list:
            if datetime.datime.now() > prom.end_date_time:
                self.__promotion_list.remove(prom)
    
    # need method that check end date time of promotion then delete it from promotion list!!!
    def remove_promotion_list(self, promotion):
        self.__promotion_list.remove(promotion)

    def search_book(self, book_id):
        for book in self.__book_list:
            if book.id == book_id:
                return book
        return None
    
    def search_reader(self, reader_id):
        for reader in self.__reader_list:
            if reader.id_account == reader_id:
                return reader
        return None
    
    def search_writer(self, writer_id):
        for writer in self.__writer_list:
            if writer.id_account == writer_id:
                return writer
        return None

    def top_up(self, account_id, amount):
        if self.search_reader(account_id) is not None:
            account = self.search_reader(account_id)
            account.balance += amount
            return True
        return False

    def show_book_info(self, book_id):
        if self.search_book(book_id) is not None:
            book = self.search_book(book_id)
            # format = [f'name : {book.name}', f'writer : {book.writer.account_name}', f'type : {book.book_type}', f'intro : {book.intro}', f'promotion : {book.promotion.show_info()}', f'rating: {book.review.rating}', f'{book.review.show_comment()}']
            return book
        return 'Not Found'
                
    def login(self, username, password):
        for account in self.__account_list:
            if account.username == username and account.password == password:
                return account
        return None

    def transfer(self, writer_id, coin):
        if self.search_writer(writer_id) is not None:
            account = self.search_writer(writer_id)
            if account.coin >= coin:
                money = coin*2
                date_time = datetime.datetime.now()
                account.money = money
                account.losing_coin = coin
                account.update_coin_transaction_history_list(coin, date_time, "Transfer")
                return "Success"
            return "You don't have enough coin"
        return "Not found your account"
    
    def rent(self, reader_id, book_id_list):
        if self.search_reader(reader_id) is not None:
            account = self.search_reader(reader_id)
            sum_price = 0
            for id in book_id_list:
                if self.search_book(id) is not None:
                    book = self.search_book(id)
                    book.update_book_status()
                    book.num_of_reader = 1
                    sum_price += (book.price_coin*0.8)
                    account.update_book_collection_list(book)
                else: return "Not found book"
                
            if account.coin >= sum_price:
                account.losing_coin = sum_price
                date_time = datetime.datetime.now()
                account.update_coin_transaction_history_list(sum_price, date_time, "Rent")
                return "Success"
            return "Don't have coin enough"
        return "Not found account"
    
    def search_book_by_promotion(self, promotion_name):
        for promotion in self.__promotion_list:
            if promotion.name_festival == promotion_name:
                books = []
                for book in promotion.book_list:
                    books.append(f'book: {book.name} price: {book.price_coin}')
                return books
        return "Not found this promotion"
    
    def add_rating(self, book_id, rating):
        if self.search_book(book_id) is not None:
            book = self.search_book(book_id)
            if book.review is None:
                book.review = Review()
            if rating < 0 or rating >5:
                return "Please rate this book in 0-5"
            else:
                book.review.add_rating(rating)
                return "Success"
        return "Not found book"