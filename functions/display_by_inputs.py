from .printer import print_title, print_book, print_book_list
from .user_inputs import input_until_valid, input_book_name, input_book_author
from .get_by_inputs import search_book, get_books_by_author

def display_books(books):
    if len(books) == 0:
        print("There are not books in the library now")
        return
    
    print_title("All Books in Library")
    print_book_list(books)

def display_book_by_name(books):
    print_title("Search Book by Name")
    name = input_until_valid(input_book_name)
    book = search_book(books, name)
    if not book:
        print("The book not found")
        return
    print_book(book)

def display_books_by_author(books):
    print_title("Display Books by Author")
    author = input_until_valid(input_book_author)
    books = get_books_by_author(books, author)
    if not books:
        print("There are no books written by this author")
        return
    print_book_list(books)
