from classes.task import *
from classes.tasklist import *

user_task_lists = []
name = input("Please enter the name of your task list")
task_list = TaskList(name)
print(task_list)