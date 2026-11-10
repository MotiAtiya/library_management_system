from .utils import clear_screen
from .user_inputs import input_until_valid, input_action_number

def show_menu():
    clear_screen()
    print("""
================================
       LIBRARY MANAGEMENT
================================

0. Exit
1. Display all books
2. Search book by name
3. Add new book
4. Borrow a book
5. Return a book
6. Display available books
7. Display books by author

Choose an option:
    """)

def get_action(num_of_options):
    action = input_until_valid(lambda: input_action_number(num_of_options))
    clear_screen()
    return action

def show_continue_msg():
    input("\n\nPress Enter to continue... ")
