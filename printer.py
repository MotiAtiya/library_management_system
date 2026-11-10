def print_title(title):
    print("* * * *  " + title + "  * * * *\n")

def print_result(result):
    if result is None:
        print("not found!")
        return
    if result == True:
        print("The operation was successful")
        return
    if result == False:
        print("The operation failed")
        return
    print(result)


def print_book(book):
    print(f"{book["id"]}. {book["name"]} by {book["author"]}, {book["year"]}")

def print_book_list(books):
    for b in books:
        print_book(b)

# def print_book(book):
#     if not book:
#         print("not found!")
#         return
#     print(f"")