from typing import List

class Task:
    def __init__(self, title: str, description: str, completed: bool) -> None:
        self.title = title
        self.description = description
        self.completed = completed

    def __str__(self) -> str:
        return f"Task is: {self.title}"
    
    def toggle_completed(self) -> None:
        self.completed = False if self.completed else True

    def change_title(self, new_title: str) -> None:
        self.title = new_title

    def change_description(self, new_description: str) -> None:
        self.description = new_description

class TaskList:
    def __init__(self, list_name: str, list_of_tasks: List[Task]) -> None:
        self.list_name = list_name
        self.list_of_tasks = list_of_tasks
    
    def __str__(self) -> str:
        res = f"{self.list_name}:\n"
        for task in self.list_of_tasks:
            res += str(task) + "\n"
        return res

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