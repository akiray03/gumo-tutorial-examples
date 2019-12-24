import typing
from todo.domain import Task, TaskKey


class TaskRepository:
    def save(self, task: Task):
        raise NotImplementedError()

    def fetch(self, key: TaskKey) -> Task:
        task = self.fetch_no_raise(key=key)
        if task is None:
            raise RuntimeError(f"Object Not Found (key={key.key_literal()}")
        return task

    def fetch_no_raise(self, key: TaskKey) -> typing.Optional[Task]:
        raise NotImplementedError()

    def fetch_list(self) -> typing.List[Task]:
        raise NotImplementedError()

    def delete(self, key: TaskKey):
        raise NotImplementedError()
