class Task:
    def __init__(self, description, state=False):
        self.description = description
        self.state = state

    def complete(self):
        self.state = True
    
    def __str__(self):
        status = "✅" if self.state else "❌"
        return f"{status} {self.description}"
    


