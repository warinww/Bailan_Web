from Book_class import Book

class Promotion:
    def __init__(self, name_festival, discount, start_date_time = None, end_date_time = None):
        self.__name_festival = name_festival
        self.__discount = discount
        self.__book_list = []
        self.__start_date_time = start_date_time
        self.__end_date_time = end_date_time

    @property
    def name_festival(self):
        return self.__name_festival

    @property
    def discount(self):
        return self.__discount

    @property
    def book_list(self):
        return self.__book_list

    @property
    def start_date_time(self):
        return self.__start_date_time

    @property
    def end_date_time(self):
        return self.__end_date_time
    
    def add_book_list(self, book):
        self.__book_list.append(book)
        book.promotion = Promotion(self.__name_festival, self.__discount, self.__start_date_time, self.__end_date_time)
    
    def show_info(self):
        return f"For {self.__name_festival} festival we give you {self.__discount} discount!"