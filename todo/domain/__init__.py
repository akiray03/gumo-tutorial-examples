import dataclasses
import datetime

from gumo.core import EntityKey
from gumo.core import NoneKey
from gumo.core import EntityKeyGenerator
from gumo.core import EntityKeyFactory
from dataclass_type_validator import dataclass_type_validator


@dataclasses.dataclass(frozen=True)
class TaskKey(EntityKey):
    KIND = "Task"
    key_generator = EntityKeyGenerator(
        key_generate_style=EntityKeyGenerator.KeyGenerateStyle.INT
    )

    @classmethod
    def build_by_id(cls, task_id: int) -> "TaskKey":
        if isinstance(task_id, str) and task_id.isdigit():
            task_id = int(task_id)
        return cls(_kind=cls.KIND, _name=task_id, _parent=NoneKey.get_instance(),)

    @classmethod
    def build_from_key(cls, key: EntityKey) -> "TaskKey":
        if key.has_parent():
            raise ValueError(f"key must not have parent: {key.key_literal()}")
        if key.kind() != cls.KIND:
            raise ValueError(f"key.KIND must equal to {cls.KIND}: {key.key_literal()}")

        return cls.build_by_id(task_id=key.name())

    @property
    def task_id(self) -> int:
        return self.name()

    @classmethod
    def build_for_new(cls) -> "TaskKey":
        incomplete_key = EntityKeyFactory().build_incomplete_key(cls.KIND)
        entity_key = cls.key_generator.generate(incomplete_key=incomplete_key)
        return cls.build_from_key(entity_key)


@dataclasses.dataclass(frozen=True)
class TaskName:
    value: str

    MAX_LENGTH = 100

    def __post_init__(self):
        dataclass_type_validator(self)

        if len(self.value) == 0:
            raise ValueError(f"TaskName must be present.")

        if len(self.value) > self.MAX_LENGTH:
            raise ValueError(f"TaskName is too long (maximum length is {self.MAX_LENGTH})")


@dataclasses.dataclass(frozen=True)
class Task:
    key: TaskKey
    name: TaskName
    created_at: datetime.datetime

    def __post_init__(self):
        dataclass_type_validator(self)
