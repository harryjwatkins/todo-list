from task import *

task_list = TaskList("TestList", [])
task_list.add_task(Task("Test Task", "Test Description"))
print(task_list.list_of_tasks[0].title)