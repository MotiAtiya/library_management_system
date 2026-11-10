from datetime import datetime

def input_until_valid(input_func):
    while True:
        try:
            return input_func()
        except ValueError as e:
            print(f"Error: {e}\n")


def input_book_name() -> str:
    name = input("Enter book name: ")
    if name.isdigit():
        raise ValueError("Book name must be a string!")
    return name


def input_book_author() -> str:
    author = input("Enter book author name: ")
    if author.isdigit():
        raise ValueError("Author name must be a string!")
    return author


def input_book_year() -> int:
    try:
        year = int(input("Enter book year: "))
    except ValueError:
        raise ValueError("Book year must be an integer number!")
    if year < 1:
        raise ValueError("Book year must be positive!")
    if year > datetime.now().year:
        raise ValueError("Book year cannot be greater then current year!")
    return year

def input_book_id() -> int:
    try:
        id = int(input("Enter book id: "))
    except ValueError:
        raise ValueError("Book year must be an integer number!")
    return id
