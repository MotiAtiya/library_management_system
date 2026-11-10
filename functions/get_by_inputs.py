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

def get_book_by_id(books, book_id):
    for b in books:
        if b["id"] == book_id:
            return b
    return None
