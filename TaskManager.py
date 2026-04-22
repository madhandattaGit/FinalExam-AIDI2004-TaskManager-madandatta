# Final Exam AIDI 2004 - Madan Datta

class TaskManager:
    def __init__(self):
        self.tasks = []

    def addTask(self, title, priority):
        self.tasks.append({"title": title, "priority": priority})


def deleteTask(self, task_id):
    """
    Deletes a task based on its ID
    """
    if 0 <= task_id < len(self.tasks):
        self.tasks.pop(task_id)