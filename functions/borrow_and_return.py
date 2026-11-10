from .user_inputs import input_until_valid, input_book_id
from .get_by_inputs import get_book_by_id

def borrow_book(books, book_id):
    book = get_book_by_id(books, book_id)

    if not book or book["available"] == False:
        return False
    
    book["available"] = False
    return True

def borrow_available_book(books):
    book_id = input_until_valid(input_book_id)
    if borrow_book(books, book_id):
        print("The book has been successfully")
    else:
        print("An error occurred while borrowing the book. The book is available at the library")

def return_book(books, book_id):
    book = get_book_by_id(books, book_id)

    if not book or book["available"] == True:
        return False
    book["available"] = True
    return True

def return_unavailable_book(books):
    book_id = input_until_valid(input_book_id)
    if return_book(books, book_id):
        print("The book was successfully returned to the library")
    else:
        print("There was a failure while returning the book, the book is not available for borrowing")
