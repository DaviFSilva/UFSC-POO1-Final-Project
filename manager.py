from models.user import User
from models.task import Task
from storage import load_data, save_data

class TaskManager:
    def __init__(self):
        self.users, self.tasks = load_data()
        self.next_user_id = max(self.users.keys(), default=0) + 1
        self.next_task_id = max([t.id for t in self.tasks], default=0) + 1

    def save(self):
        save_data(self.users, self.tasks)

    # Users CRUD
    def register_user(self, name: str, email: str) -> User:
        new_user = User(self.next_user_id, name, email)
        self.users[new_user.id] = new_user
        self.next_user_id += 1
        return new_user

    def list_users(self) -> list:
        return list(self.users.values())

    def get_user(self, user_id: int) -> User:
        return self.users.get(user_id)

    # Tasks CRUD
    def create_task(self, title: str, description: str) -> Task:
        new_task = Task(self.next_task_id, title, description)
        self.tasks.append(new_task)
        self.next_task_id += 1
        return new_task

    def get_all_tasks(self) -> list:
        return self.tasks
        
    def get_task(self, task_id: int) -> Task:
        for t in self.tasks:
            if t.id == task_id:
                return t
        return None

    def delete_task(self, task_id: int) -> bool:
        task = self.get_task(task_id)
        if task:
            self.tasks.remove(task)
            return True
        return False

    # Filters
    def filter_by_status(self, status: str) -> list:
        return [t for t in self.tasks if t.status.lower() == status.lower()]

    def filter_by_assignee(self, user_id: int) -> list:
        user_tasks = []
        for t in self.tasks:
            for assignee in t.assignees:
                if assignee.id == user_id:
                    user_tasks.append(t)
                    break
        return user_tasks

    def filter_by_tag(self, tag: str) -> list:
        return [t for t in self.tasks if tag.lower() in t.tags]
