from typing import List

class Task:
    def __init__(self, title: str, description: str, completed: bool) -> None:
        self.title = title
        self.description = description
        self.completed = completed

    def __str__(self) -> str:
        return f"Task is: {self.title}"
    
    def mark_as_not_completed(self) -> None:
        self.completed = False
    
    def mark_as_completed(self) -> None:
        self.completed = True
    
    def toggle_completed(self) -> None:
        self.completed = False if self.completed else True

    def change_title(self, new_title: str) -> None:
        self.title = new_title

    def change_description(self, new_description: str) -> None:
        self.description = new_description