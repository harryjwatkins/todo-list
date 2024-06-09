from classes.task import *
from classes.tasklist import *

user_task_lists = []

def display_main_menu():
    print("What would you like to do:")
    print("1) Create task list")
    print("2) View task lists")
    print("3) Edit task list")
    print("4) Quit program")

def get_main_menu_choice():
    while True:
        user_input = input("Please enter your choice:")
        if user_input not in ["1", "2", "3", "4"]:
            print("Invalid input")
            continue
        return user_input

def display_task_lists():
    if len(user_task_lists) == 0:
        print("There are no created task lists")
        return

    print("These are your current task lists:")
    for index, task_list in enumerate(user_task_lists):
        print(index + 1, ")", task_list.list_name)
    
def get_user_task_list_choice():
    n = len(user_task_lists)
    while True:
        user_choice = input("Please choose task list")
        if int(user_choice) in range(1, n+1):
            return int(user_choice) - 1
        print("Please enter valid value")
    
def create_task_list() -> None:
    task_list_name = input("What would you like to call the list?")
    created_task_list = TaskList(task_list_name)
    user_task_lists.append(created_task_list)

def display_edit_task_list_main_menu() -> None:
    display_task_lists()
    print("Which task list would you like to edit:")

def display_edit_task_list_choices() -> None:
    print("1) Add task")
    print("2) Remove task")
    print("3) Mark task as completed/todo")
    print("4) Rename task")
    print("What would you like to do:")

def add_task_to_task_list(task_list: TaskList):
    title = input("What task would you like to add?")
    description = input("Please enter a description of the task")
    new_task = Task(title, description)
    task_list.add_task(new_task)

def remove_task_from_task_list(task_list: TaskList):
    print(task_list)
    while True: 
        user_choice = input("Which task would you like to delete?")
        if int(user_choice) in range(1, len(task_list.list_of_tasks)+1):
            break     
        print("That was an invalid choice, please try again")   
    del(task_list.list_of_tasks[int(user_choice)-1])

def toggle_task_in_task_list(task_list: TaskList):
    print(task_list)
    while True: 
        user_choice = input("Which task would you like to toggle?")
        if int(user_choice) in range(1, len(task_list.list_of_tasks)+1):
            break
        print("That was an invalid choice, please try again")        
    task_list.list_of_tasks[int(user_choice)-1].toggle_completed()

def rename_task_in_task_list(task_list: TaskList):
    print(task_list)
    while True: 
        user_choice = input("Which task would you like rename?")
        if int(user_choice) in range(1, len(task_list.list_of_tasks)+1):
            break
        print("That was an invalid choice, please try again")
    rename = input("What would you like to rename it to?")        
    task_list.list_of_tasks[int(user_choice)-1].change_title(rename)

def get_edit_task_list_choice():
    valid_choices = ["1", "2", "3", "4"]
    while True:
        user_choice = input()
        if user_choice in valid_choices:
            return user_choice
        print("Please enter valid value")

def edit_controller(user_choice, task_list):
    if user_choice == '1':
        add_task_to_task_list(task_list)
    elif user_choice == '2':
        remove_task_from_task_list(task_list)
    elif user_choice == '3':
        toggle_task_in_task_list(task_list)
    else:
        rename_task_in_task_list(task_list)
    
def remove_task_list_main():
        display_task_lists()
        user_choice = get_user_task_list_choice()
        print(user_task_lists[user_choice])

def mark_task_list_main():
        display_edit_task_list_main_menu()
        user_choice = get_user_task_list_choice()
        task_list_to_edit = user_task_lists[user_choice]
        display_edit_task_list_choices()
        user_choice = get_edit_task_list_choice()
        edit_controller(user_choice, task_list_to_edit)

def select_main_menu_option(choice: str) -> None:
    if choice == '1':
        create_task_list()
    elif choice == '2':
        remove_task_list_main()
    elif choice == '3':
        mark_task_list_main()
    elif choice == '4':
        print("Thanks for using this program, goodbye")
        exit()

while True:
    display_main_menu()
    user_choice = get_main_menu_choice()
    select_main_menu_option(user_choice)
