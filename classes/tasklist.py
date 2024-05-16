from typing import List
from classes.task import Task

class TaskList:
    def __init__(self, list_name: str, list_of_tasks: List[Task]) -> None:
        self.list_name = list_name
        self.list_of_tasks = list_of_tasks
    
    def __str__(self) -> str:
        res = f"{self.list_name}:\n"
        for task in self.list_of_tasks:
            res += str(task) + "\n"
        return res
    
    def change_list_name(self, new_name: str) -> None:
        self.list_name = new_name

    def add_task(self, task: Task) -> None:
        self.list_of_tasks.append(task)
        print("Task was added to TaskList: {self.list_name}")
    
    def remove_task(self, task_to_remove: Task) -> None:
        try:
            self.list_of_tasks.remove(task_to_remove)
        except:
            print("Unable to remove task as does not exist in the task list")
            return
        print(f"Task {task_to_remove.title} was removed")