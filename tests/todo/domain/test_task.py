import datetime
import pytest

from gumo.core import EntityKeyFactory
from dataclass_type_validator import TypeValidationError

from todo.domain import Task, TaskKey, TaskName


class TestTaskKey:
    def test_equal(self):
        key1 = TaskKey.build_by_id(task_id=1)
        key2 = TaskKey.build_by_id(task_id=1)
        assert key1 == key2
        assert key1.task_id == 1

    def test_build_from_key(self):
        entity_key = EntityKeyFactory().build(kind="Task", name=1,)
        task_key = TaskKey.build_from_key(key=entity_key)
        assert entity_key != task_key
        assert entity_key.key_literal() == task_key.key_literal()


class TestTask:
    def test_build_successful(self):
        task = Task(
            key=TaskKey.build_by_id(task_id=1),
            name=TaskName("Task Name"),
            finished_at=None,
            created_at=datetime.datetime(
                2019, 12, 1, 0, 0, 0, tzinfo=datetime.timezone.utc
            ),
            updated_at=datetime.datetime(
                2019, 12, 1, 0, 0, 0, tzinfo=datetime.timezone.utc
            ),
        )
        assert isinstance(task, Task)

    def test_build_failure(self):
        with pytest.raises(expected_exception=TypeValidationError):
            Task(
                key=TaskKey.build_by_id(task_id=1),
                name="task name",
                finished_at=None,
                created_at=datetime.datetime(
                    2019, 12, 1, 0, 0, 0, tzinfo=datetime.timezone.utc
                ),
                updated_at=datetime.datetime(
                    2019, 12, 1, 0, 0, 0, tzinfo=datetime.timezone.utc
                ),
            )

    def test_finished_property(self):
        task = Task(
            key=TaskKey.build_by_id(task_id=1),
            name=TaskName("Task Name"),
            finished_at=None,
            created_at=datetime.datetime(
                2019, 12, 1, 0, 0, 0, tzinfo=datetime.timezone.utc
            ),
            updated_at=datetime.datetime(
                2019, 12, 1, 0, 0, 0, tzinfo=datetime.timezone.utc
            ),
        )
        assert not task.is_finished

        finished_task = Task(
            key=TaskKey.build_by_id(task_id=1),
            name=TaskName("Task Name"),
            finished_at=datetime.datetime(
                2019, 12, 2, 0, 0, 0, tzinfo=datetime.timezone.utc
            ),
            created_at=datetime.datetime(
                2019, 12, 1, 0, 0, 0, tzinfo=datetime.timezone.utc
            ),
            updated_at=datetime.datetime(
                2019, 12, 1, 0, 0, 0, tzinfo=datetime.timezone.utc
            ),
        )
        assert finished_task.is_finished
