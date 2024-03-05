from Payment_history_class import PaymentHistory
from Coin_transaction_class import Coin_transaction

class Account:
    def __init__(self, account_name, password):
        self.__account_name = account_name
        self.__password = password

    @property
    def account_name(self):
        return self.__account_name

    @property
    def password(self):
        return self.__password
    
    @property
    def id_account(self):
        return self.__id_account

class Reader(Account):
    def __init__(self, account_name, password):
        super().__init__(account_name, password)
        self.__id_account = 0
        self.__book_collection_list = []
        self.__cart_list = []
        self.__coin = 0
        self.__payment_history_list = []
        self.__coin_transaction_history_list = []

    @property
    def id_account(self):
        return self.__id_account

    @property
    def book_collection_list(self):
        return self.__book_collection_list

    @property
    def cart(self):
        return self.__cart
    
    @property
    def coin(self):
        return self.__coin
    
    @property
    def payment_history_list(self):
        return self.__payment_history_list

    @property
    def coin_transaction_history_list(self):
        return self.__coin_transaction_history_list
    
    @id_account.setter
    def id_account(self, id_account):
        self.__id_account = id_account

    @coin.setter
    def adding_coin(self, adding_coin):
        self.__coin += adding_coin
        
    @coin.setter
    def losing_coin(self, losing_coin):
        self.__coin -= losing_coin

    def update_payment_history_list(self, payment_history):
        self.__payment_history_list.append(payment_history)

    def update_coin_transaction_history_list(self, coin,date_time,type):
        self.__coin_transaction_history_list.append(Coin_transaction(coin,date_time,type))

    def update_book_collection_list(self, book):
        self.__book_collection_list.append(book)

    def update_cart_of_book_list(self, book):
        self.__cart_list.append(book)

class Writer(Account):
    def __init__(self, account_name, password):
        super().__init__(account_name, password)
        self.__id_account = 0
        self.__book_collection_list = []
        self.__coin = 0
        self.__money = 0
        self.__coin_transaction_history_list = []

    @property
    def id_account(self):
        return self.__id_account

    @property
    def coin(self):
        return self.__coin
    
    @property
    def money(self):
        return self.__money

    @property
    def book_collection_list(self):
        return self.__book_collection_list
    
    @property
    def coin_transaction_history_list(self):
        return self.__coin_transaction_history_list
    
    @id_account.setter
    def id_account(self, id_account):
        self.__id_account = id_account
    
    @money.setter
    def money(self, adding_money):
        self.__money += adding_money
        
    @coin.setter
    def adding_coin(self, adding_coin):
        self.__coin += adding_coin
        
    @coin.setter
    def losing_coin(self, losing_coin):
        self.__coin -= losing_coin

    def get_review(self):
        pass

    def update_book_collection_list(self, book):
        self.__book_collection_list.append(book)

    def update_coin_transaction_history_list(self,coin,date_time,type):
        self.__coin_transaction_history_list.append(Coin_transaction(coin,date_time,type))