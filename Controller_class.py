class Controller:
    def __init__(self):
        self.__reader_list = []
        self.__writer_list = []
        self.__complain_list = []
        self.__book_list = []
        self.__payment_method_list = []

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

    def add_reader(self, reader):
        self.__reader_list.append(reader)
        
    def add_writer(self, writer):
        self.__writer_list.append(writer)

    def add_complain(self, complain):
        self.__complain_list.append(complain)

    def add_book(self, book):
        self.__book_list.append(book)

    def add_payment_method(self, payment_method):
        self.__payment_method_list.append(payment_method)

    def search_book(self, book_id):
        for book in self.__book_list:
            if book.id == book_id:
                return book
        return None

    def top_up(self, account_id, amount):
        for account in self.__account_list:
            if account.id == account_id:
                account.balance += amount
                return True
        return False

    def show_book_info(self, book_id):
        for book in self.__book_list:
            if book.id == book_id:
                format = [f'name : {book.name}', f'writer : {book.writer.account_name}', f'type : {book.book_type}', f'intro : {book.intro}', f'promotion : {book.promotion.show_info()}', f'rating: {book.review.rating}', f'{book.review.show_comment()}']
                return format
            return 'Not Found'
        return 'Not Found'

                
    def login(self, username, password):
        for account in self.__account_list:
            if account.username == username and account.password == password:
                return account
        return None

    def transfer(self, sender_account_id, receiver_account_id, amount):
        sender_account = self.login(sender_account_id, None)
        receiver_account = self.login(receiver_account_id, None)
        if sender_account and receiver_account:
            if sender_account.balance >= amount:
                sender_account.balance -= amount
                receiver_account.balance += amount
                return True
        return False