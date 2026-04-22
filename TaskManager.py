# Final Exam AIDI 2004 - Madan Datta

class TaskManager:
    def __init__(self):
        self.tasks = []

    def addTask(self, title, priority):
        self.tasks.append({"title": title, "priority": priority})