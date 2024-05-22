from classes.task import *
from classes.tasklist import *

def display_main_menu():
    print("What would you like to do:")
    print("1) Create task list")
    print("2) View task lists")
    print("3) Quit program")

def get_main_menu_choice():
    while True:
        user_input = input("Please enter your choice:")
        if user_input not in ["1", "2", "3"]:
            print("Invalid input")
            continue
        return user_input

def view_task_lists():
    raise NotImplementedError()

def create_task_list():
    raise NotImplementedError()

def select_main_menu_option(choice: str) -> None:
    if choice == '1':
        create_task_list()
    elif choice == '2':
        view_task_lists()
    else:
        print("Thanks for using this program, goodbye")
        exit()

user_task_lists = []
while True:
    display_main_menu()
    user_choice = get_main_menu_choice()
    select_main_menu_option(user_choice)
