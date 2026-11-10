from printer import print_title, print_book_list, print_book
from user_inputs import input_until_valid, input_book_author, input_book_name, input_book_year, input_book_id
def display_books(books):
    if len(books) == 0:
        print("There are not books in the library now")
        return
    
    print_title("All Books in Library")
    for b in books:
        print(b["name"])


def search_book(books, name):
    for b in books:
        if b["name"].lower() == name.lower():
            return b
    return None

def get_books_by_author(books, author):
    return list(filter(lambda b: b["author"] == author ,books))

def get_books_by_name_and_author(books, name, author):
    return search_book(get_books_by_author(books, author), name)


def get_next_book_id(books):
    current_last_id = max(books, key=lambda b: b["id"])["id"]
    return current_last_id +1


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


def get_book_by_id(books, book_id):
    for b in books:
        if b["id"] == book_id:
            return b
    return None


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


def get_available_books(books):
    return list(filter(lambda b: b["available"] ,books))

def display_available_books(books):
    avilables = get_available_books(books)
    if len(avilables) == 0:
        print("There are not available books now")
        return
    
    print_title("Available Books")
    print_book_list(avilables)

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
