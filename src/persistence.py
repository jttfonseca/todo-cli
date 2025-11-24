import json
import os
from typing import Optional
from src.todolist import TodoList
from src.task import Task

DEFAULT_PATH = "data/tasks.json"


def save_to_file(todo_list: TodoList, filename: Optional[str] = None) -> None:
    """Serialize a TodoList (name + tasks) to a JSON file."""
    path = filename or DEFAULT_PATH
    os.makedirs(os.path.dirname(path), exist_ok=True)

    data = {
        "name": todo_list.name,
        "tasks": [t.to_dict() for t in todo_list.tasks],
    }

    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

    print(f"💾 Saved {len(todo_list.tasks)} tasks to {path}")


def load_from_file(filename: Optional[str] = None) -> TodoList:
    """Load a TodoList from a JSON file. If not found/corrupted, return an empty list."""
    path = filename or DEFAULT_PATH

    if not os.path.exists(path):
        print("⚠️ No saved data found. Returning an empty list.")
        return TodoList("Personal")

    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except json.JSONDecodeError:
        print("⚠️ JSON file is corrupted or invalid. Returning an empty list.")
        return TodoList("Personal")

    name = data.get("name", "Personal")
    todo = TodoList(name)
    for item in data.get("tasks", []):
        todo.add(Task.from_dict(item))

    print(f"📥 Loaded {len(todo.tasks)} tasks from {path}")
    return todo
