# TODO: Create a Book class with the following instance variables:
# name
# author
# user_rating
# number_of_reviews
# price
# year
# genre

class Book:
    def __init__(self, book_dictionary):
        self.id = book_dictionary['id']
        self.name = book_dictionary['name']
        self.author = book_dictionary['author']
#        self.user_rating = book_dictionary['user rating']
        self.number_of_reviews = book_dictionary['number_of_reviews']
        self.price = book_dictionary['price']
        self.year = book_dictionary['year']
        self.genre = book_dictionary['genre']