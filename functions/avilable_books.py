from .printer import print_title, print_book_list

def get_available_books(books):
    return list(filter(lambda b: b["available"] ,books))

def display_available_books(books):
    avilables = get_available_books(books)
    if len(avilables) == 0:
        print("There are not available books now")
        return
    
    print_title("Available Books")
    print_book_list(avilables)
