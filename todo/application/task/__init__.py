import datetime

from injector import inject

from todo.application.task.repository import TaskRepository
from todo.domain import Task
from todo.domain import TaskKey
from todo.domain import TaskName


class TaskCreateService:
    @inject
    def __init__(self, task_repository: TaskRepository):
        self.task_repository = task_repository

    def execute(self, task_name: str) -> Task:
        task = Task(
            key=TaskKey.build_for_new(),
            name=TaskName(task_name),
            created_at=datetime.datetime.utcnow().astimezone(tz=datetime.timezone.utc),
        )
        self.task_repository.save(task=task)

        return task
