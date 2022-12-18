from data import data_list
from book import Book

def run_analysis(book_list):
    books = create_book_list(book_list)
    print('')
    print("*******************************************************************")
    print('')
    example_analysis(books)
    print('')
    print("*******************************************************************")
    print('')
    analysis_one(books)
    print('')
    print("*******************************************************************")
    print('')
    analysis_two(books)
    print('')
    print("*******************************************************************")
    print('')
    analysis_three(books)


def create_book_list(data_list):
    book_list = []
    # TODO: Write a function that will loop through data_list, and create a Book object for each list item
    for book in data_list:
        new_book = Book(book)
    # TODO: Then, add each Book item to book_list
        book_list.append(new_book)
    # TODO: Finally, return book_list for use in analysis questions!
    return book_list


def example_analysis(book_list):
    print("Analysis of which book had the highest price in 2016")
    # Find all books from 2016
    # Use a Lambda filter function to find books who have a year of 2016
    # Converting to a list, and saving as variable books_2016
    books_2016 = list(filter(lambda book: book.year == 2016, book_list))
    # Calculating the maximum price, and saving that book as highest_cost_book
    # Using max(), with Lambda function
    highest_cost_book = max(books_2016, key=lambda book: book.price)
    # Print that book's name & price to terminal
    print(
        f"The most expensive book in 2016 was {highest_cost_book.name} with a price of {highest_cost_book.price}")


def analysis_one(book_list):
    print("Analysis of which book had the lowest number of reviews in 2018")
    # Find all books from 2018
    # Use a lambda filter function to find books who have a year of 2018
    # Converting to a list and saving as variable books_2018
    books_2018 = list(filter(lambda book: book.year == 2018, book_list))
    # Calculating the minimum number of reviews and saving that book as lowest_review_book
    # Using min() with lambda function
    lowest_review_book = min(books_2018, key=lambda book: book.number_of_reviews)
    # Print that book's name & number of reviews to terminal
    print(
        f"The book with the lowest number of reviews in 2018 was {lowest_review_book.name} with {lowest_review_book.number_of_reviews} reviews")

def analysis_two(book_list):
    print("Analysis of which genre (fiction or non-fiction) has appeared the most in the top 50's list")
    # Use a lambda filter function to find books who have a genre of fiction
    fiction_books = list(filter(lambda book: book.genre == "Fiction", book_list))
    # Use a lambda filter function to find books who have a genre of non-fiction
    non_fiction_books = list(filter(lambda book: book.genre == "Non Fiction", book_list))
    # Print the number of books in each genre to terminal
    print(
        f"There are {len(fiction_books)} fiction books and {len(non_fiction_books)} non-fiction books in the top 50")
    print ("Non fiction books appear more often in the top 50 list")

def analysis_three(book_list):
    print("Analysis of which book appeared most often in top 50's list, and how often it appeared")
    # Create  dictioary from to hold most common book name and count
    # Create a list of book names
    book_name_list = [book['name'] for book in book_list]
    # Loop through unique book names to find the most common book name
    best_book = {"name":"book name", "count": 0}  
    # Use a lambda filter function to find books who have a name of book_name
    # Use len() to find the number of books with that name
    unique_book_names = set(book_name_list)      
    for book_name in unique_book_names:
            results = len(
                list(filter(lambda name: name == book_name, book_name_list)))

    if results > best_book["count"]:
            best_book["count"] = results
            best_book["name"] = book_name
     # Print the most common book name and count to terminal
    print(
        f"The book that appears the most in the top 50 list is {best_book['name']} with {best_book['count']} appearances")
    

# BONUS USER STORIES:


#def bonus_analysis_one(book_list):
#    print("Analysis of which author has shown up on the top 50's list the most (Distinct books only!)")


#def bonus_analysis_two(book_list):
#    print("Analysis of the top book for each year, based on the book's user ratings and number of reviews")


#def bonus_analysis_three(book_list):
#    print("Analysis of which book has appeared the most consecutively on top 50's list")


run_analysis(data_list)
