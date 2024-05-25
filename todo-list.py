from classes.task import *
from classes.tasklist import *

user_task_lists = []

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

def display_task_lists():
    print("These are your current task lists:")
    for index, task_list in enumerate(user_task_lists):
        print(index, ")", task_list.list_name)

def get_user_task_list_choice():
    n = len(user_task_lists)
    while True:
        user_choice = input("Please choose task list to view")
        if user_choice in range(1, n):
            return user_choice
        print("Please enter valid value")
    


def create_task_list() -> None:
    task_list_name = input("What would you like to call the list?")
    created_task_list = TaskList(task_list_name)
    user_task_lists.append(created_task_list)

def select_main_menu_option(choice: str) -> None:
    if choice == '1':
        create_task_list()
    elif choice == '2':
        display_task_lists()
    else:
        print("Thanks for using this program, goodbye")
        exit()

while True:
    display_main_menu()
    user_choice = get_main_menu_choice()
    select_main_menu_option(user_choice)
