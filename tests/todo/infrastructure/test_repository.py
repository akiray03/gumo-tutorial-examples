import main
import datetime

from gumo.datastore.infrastructure.test_utils import DatastoreRepositoryMixinForTest
from todo.application.task.repository import TaskRepository
from todo.domain import Task, TaskKey, TaskName


class TestTaskRepository(DatastoreRepositoryMixinForTest):
    KIND = TaskKey.KIND
    repository: TaskRepository = main.injector.get(TaskRepository)

    def test_save(self):
        self.cleanup_entities()
        assert self.count_entities() == 0

        task = Task(
            key=TaskKey.build_by_id(task_id=123),
            name=TaskName("Task Name"),
            finished_at=None,
            created_at=datetime.datetime(2019, 12, 1, tzinfo=datetime.timezone.utc),
            updated_at=datetime.datetime(2019, 12, 1, tzinfo=datetime.timezone.utc),
        )
        self.repository.save(task=task)
        assert self.count_entities() == 1

    def test_save_and_fetch(self):
        self.cleanup_entities()

        task = Task(
            key=TaskKey.build_by_id(task_id=123),
            name=TaskName("Task Name"),
            finished_at=None,
            created_at=datetime.datetime(2019, 12, 1, tzinfo=datetime.timezone.utc),
            updated_at=datetime.datetime(2019, 12, 1, tzinfo=datetime.timezone.utc),
        )
        self.repository.save(task=task)
        fetched_task = self.repository.fetch(key=task.key)
        assert fetched_task == task
