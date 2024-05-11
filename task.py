class Task:
    def __init__(self, title, description) -> None:
        self.title = title
        self.description = description

class TaskList:
    def __init__(self, list_name, list_of_tasks) -> None:
        self.list_name = list_name
        self.list_of_tasks = list_of_tasks