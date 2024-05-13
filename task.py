from typing import List

class Task:
    def __init__(self, title: str, description: str) -> None:
        self.title = title
        self.description = description

    def __str__(self) -> str:
        return f"Task is: {self.title}"

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