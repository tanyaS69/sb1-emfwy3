class TodoManager:
    def __init__(self):
        self.todos = []

    def add_todo(self, title, description=""):
        todo = {
            "id": len(self.todos) + 1,
            "title": title,
            "description": description,
            "completed": False
        }
        self.todos.append(todo)
        return todo

    def get_all_todos(self):
        return self.todos

    def get_todo(self, todo_id):
        return next((todo for todo in self.todos if todo["id"] == todo_id), None)

    def update_todo(self, todo_id, title=None, description=None, completed=None):
        todo = self.get_todo(todo_id)
        if todo:
            if title is not None:
                todo["title"] = title
            if description is not None:
                todo["description"] = description
            if completed is not None:
                todo["completed"] = completed
            return todo
        return None

    def delete_todo(self, todo_id):
        todo = self.get_todo(todo_id)
        if todo:
            self.todos.remove(todo)
            return True
        return False