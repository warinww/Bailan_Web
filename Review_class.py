import datetime

class Review:
    def __init__(self):
        self.__rating = None
        self.__rating_list = []
        self.__comment_list = []
        
    @property
    def rating(self):
        return self.__rating

    @property
    def rating_list(self):
        return self.__rating_list

    @property
    def comment_list(self):
        return self.__comment_list
    
    @property
    def comment_dict(self):
        return self.__comment_dict
    
    def add_rating(self, rating):
        self.__rating_list.append(rating)
        self.__rating = sum(self.__rating_list) / len(self.__rating_list)
    
    def add_comment(self, reader, comment):
        date_time = datetime.datetime.now()
        self.__comment_list.append((reader, comment, date_time))
        
    def show_comment(self):
        format = []
        for account, comment, date_time in self.__comment_list:
            format.append(f"{account} account : {comment} on {date_time}")
        return format