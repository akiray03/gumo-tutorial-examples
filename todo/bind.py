from todo.application.task.repository import TaskRepository
from todo.infrastructure.task.repository import DatastoreTaskRepository


def bind_todo(binder):
    binder.bind(TaskRepository, to=DatastoreTaskRepository)
