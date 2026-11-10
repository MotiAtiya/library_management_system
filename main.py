from initial_data import get_books


def display_books(books):
    for b in books:
        print(b["name"])


def search_book(books, name):
    for b in books:
        if b["name"] == name:
            return b
    return None

def add_book(books, name, author, year):
    new_book = {
        "name": name,
        "author": author,
        "year": year,
        "available":True
    }
    books.append(new_book)

    return new_book in books

# def borrow_book(books, book_id):
#     book = 

def main():
    books = get_books()

    display_books(books)


if __name__ == "__main__":
    main()