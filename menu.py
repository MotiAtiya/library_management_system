from utils import clear_screen

def show_menu():
    clear_screen()
    print("""
================================
       LIBRARY MANAGEMENT
================================

1. Display all books
2. Search book by name
3. Add new book
4. Borrow a book
5. Return a book
6. Display available books
7. Display books by author
8. Exit

Choose an option:
    """)

def get_action():
    action = int(input())
    clear_screen()
    return action


def show_continue_msg():
    input("\n\nPress Enter to continue... ")
