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
        now = datetime.datetime.utcnow().astimezone(tz=datetime.timezone.utc)
        task = Task(
            key=TaskKey.build_for_new(),
            name=TaskName(task_name),
            finished_at=None,
            created_at=now,
            updated_at=now,
        )
        self.task_repository.save(task=task)

        return task


class TaskUpdateService:
    @inject
    def __init__(self, task_repository: TaskRepository):
        self.task_repository = task_repository

    def execute(self, key: TaskKey, finished: bool) -> Task:
        task = self.task_repository.fetch(key=key)

        if finished:
            modified_task = task.to_finished_now()
        else:
            modified_task = task.with_finished_at(finished_at=None)

        self.task_repository.save(task=modified_task)

        return modified_task
