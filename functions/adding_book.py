from .printer import print_title
from .user_inputs import input_until_valid, input_book_name, input_book_author, input_book_year
from .get_by_inputs import get_books_by_name_and_author, get_next_book_id


def add_book(books, name, author, year):
    if not name or not author or year < 1:
        return False

    if get_books_by_name_and_author(books, name, author):
        return False
    
    new_book = {
        "id": get_next_book_id(books),
        "name": name,
        "author": author,
        "year": year,
        "available":True
    }
    books.append(new_book)

    return new_book in books

def add_new_book_by_inputs(books):
    print_title("Add a New Book")
    name = input_until_valid(input_book_name)
    author = input_until_valid(input_book_author)
    year = input_until_valid(input_book_year)

    if add_book(books, name, author, year):
        print(f"The book '{name}' was successfully added to the library")
    else:
        print("An error occurred while adding the book")
