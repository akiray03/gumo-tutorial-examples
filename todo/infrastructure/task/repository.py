import typing
from gumo.datastore.infrastructure import DatastoreRepositoryMixin
from gumo.datastore.infrastructure import DatastoreEntity

from todo.application.task.repository import TaskRepository
from todo.domain import Task, TaskKey, TaskName
from . import TaskDataModel


class DatastoreTaskRepository(DatastoreRepositoryMixin, TaskRepository):
    def save(self, task: Task):
        model = TaskDataModel(
            key=self.to_datastore_key(entity_key=task.key),
            name=task.name.value,
            created_at=task.created_at,
        )
        doc = model.to_datastore_entity()
        self.datastore_client.put(doc)

    def fetch_no_raise(self, key: TaskKey) -> typing.Optional[Task]:
        datastore_key = self.to_datastore_key(entity_key=key)
        doc = self.datastore_client.get(key=datastore_key)
        if doc is None:
            return None

        return self._to_domain_entity(doc=doc)

    def _to_domain_entity(self, doc: DatastoreEntity) -> Task:
        model = TaskDataModel.from_datastore_entity(doc=doc)
        return Task(
            key=TaskKey.build_from_key(key=self.to_entity_key(datastore_key=model.key)),
            name=TaskName(model.name),
            created_at=model.created_at,
        )

    def fetch_list(self) -> typing.List[Task]:
        query = self.datastore_client.query(kind=TaskKey.KIND)
        tasks = [
            self._to_domain_entity(doc=doc)
            for doc in query.fetch()
        ]
        return tasks
