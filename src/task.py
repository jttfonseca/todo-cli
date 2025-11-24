class Task:
    def __init__(self, description: str, completed: bool = False):
        self.description = description
        self.completed = completed

    def complete(self) -> None:
        self.completed = True

    def to_dict(self) -> dict:
        return {"description": self.description, "completed": self.completed}

    @classmethod
    def from_dict(cls, data: dict) -> "Task":
        return cls(
            description=data["description"],
            completed=bool(data.get("completed", False)),
        )

    def __str__(self) -> str:
        status = "✅" if self.completed else "❌"
        return f"{status} {self.description}"



