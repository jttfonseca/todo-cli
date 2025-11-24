from typing import List
from src.task import Task


class TodoList:
    def __init__(self, name: str):
        self.name: str = name
        self.tasks: List[Task] = []

    def add(self, task: Task) -> None:
        if not isinstance(task, Task):
            raise TypeError("add() expects a Task instance")
        self.tasks.append(task)

    def remove(self, index: int) -> None:
        if index < 1 or index > len(self.tasks):
            print("⚠️ Invalid index")
            return
        removed = self.tasks.pop(index - 1)
        print(f"🗑️ Removed: {removed.description}")

    def complete(self, index: int) -> None:
        if index < 1 or index > len(self.tasks):
            print("⚠️ Invalid index")
            return
        self.tasks[index - 1].complete()
        print(f"✅ Completed: {self.tasks[index - 1].description}")

    def list_tasks(self) -> None:
        if not self.tasks:
            print("No tasks in the list.")
            return
        print(f"To-Do List: {self.name}")
        for i, task in enumerate(self.tasks, start=1):
            print(f"{i}. {task}")
