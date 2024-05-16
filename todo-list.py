from classes.task import *
from classes.tasklist import *

task_list = TaskList("TestList", [])
task_list.add_task(Task("Test Task", "Test Description"))
print(task_list)