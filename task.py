from typing import List

class Task:
    def __init__(self, title: str, description: str) -> None:
        self.title = title
        self.description = description

class TaskList:
    def __init__(self, list_name: str, list_of_tasks: List[Task]) -> None:
        self.list_name = list_name
        self.list_of_tasks = list_of_tasks

    def add_task(self, task: Task) -> None:
        self.list_of_tasks.append(task)
        print("Task was added to TaskList: {self.list_name}")