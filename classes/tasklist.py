from typing import List
from classes.task import Task

class TaskList:
    def __init__(self, list_name: str) -> None:
        self.list_name = list_name
        self.list_of_tasks = []
    
    def __str__(self) -> str:
        res = f"{self.list_name}:\n"
        for task in self.list_of_tasks:
            res += str(task) + "\n"
        return res
    
    def change_list_name(self, new_name: str) -> None:
        if self.list_name == new_name:
            raise Exception("Cannot change a list to the same name")
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
    
    def mark_all_as_done(self) -> None:
        for task in self.list_of_tasks:
            if task.completed:
                continue
            task.mark_as_completed()

    def mark_all_as_todo(self) -> None:
        for task in self.list_of_tasks:
            if not task.completed:
                continue
            task.mark_as_not_completed()