import datetime
import dataclasses

from gumo.datastore.infrastructure import DataModel
from gumo.datastore.infrastructure import DatastoreEntity
from gumo.datastore.infrastructure import DatastoreKey


@dataclasses.dataclass()
class TaskDataModel(DataModel):
    exclude_from_indexes = []

    key: DatastoreKey
    name: str
    created_at: datetime.datetime

    def to_datastore_entity(self) -> DatastoreEntity:
        doc = DatastoreEntity(
            key=self.key, exclude_from_indexes=self.exclude_from_indexes,
        )
        doc.update(
            {
                "name": self.name,
                "created_at": self.created_at,
            }
        )
        return doc

    @classmethod
    def from_datastore_entity(cls, doc: DatastoreEntity) -> "TaskDataModel":
        return cls(
            key=doc.key,
            name=doc["name"],
            created_at=cls.convert_datetime(doc["created_at"]),
        )
