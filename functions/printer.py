def print_title(title):
    print("* * * *  " + title + "  * * * *\n")

def print_book(book):
    print(f"{book["id"]}. {book["name"]} by {book["author"]}, {book["year"]}")

def print_book_list(books):
    for b in books:
        print_book(b)
