from DATA.initial_data import get_books
from functions.menu import show_menu, get_action, show_continue_msg
from functions.display_by_inputs import display_books, display_book_by_name, display_books_by_author
from functions.adding_book import add_new_book_by_inputs
from functions.borrow_and_return import borrow_available_book, return_unavailable_book
from functions.avilable_books import display_available_books

def exit_program():
    print("Bye!")
    exit(0)

ACTIONS = {
    1: display_books,
    2: display_book_by_name,
    3: add_new_book_by_inputs,
    4: borrow_available_book,
    5: return_unavailable_book,
    6: display_available_books,
    7: display_books_by_author
}

def main():
    books = get_books()

    while True:
        try:
            show_menu()
            action = get_action()

            if action == 8:
                print("Bye!")
                exit(0)
            
            ACTIONS[action](books)

            show_continue_msg()

        except ValueError as e:
            print(e)


if __name__ == "__main__":
    main()