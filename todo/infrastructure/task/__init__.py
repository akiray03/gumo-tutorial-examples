import datetime
import dataclasses
from typing import Optional

from gumo.datastore.infrastructure import DataModel
from gumo.datastore.infrastructure import DatastoreEntity
from gumo.datastore.infrastructure import DatastoreKey


@dataclasses.dataclass()
class TaskDataModel(DataModel):
    exclude_from_indexes = []

    key: DatastoreKey
    name: str
    finished_at: Optional[datetime.datetime]
    created_at: datetime.datetime
    updated_at: datetime.datetime

    def to_datastore_entity(self) -> DatastoreEntity:
        doc = DatastoreEntity(
            key=self.key, exclude_from_indexes=self.exclude_from_indexes,
        )
        doc.update(
            {
                "name": self.name,
                "finished_at": self.finished_at,
                "created_at": self.created_at,
                "updated_at": self.updated_at,
            }
        )
        return doc

    @classmethod
    def from_datastore_entity(cls, doc: DatastoreEntity) -> "TaskDataModel":
        return cls(
            key=doc.key,
            name=doc["name"],
            finished_at=cls.convert_optional_datetime(doc.get("finished_at")),
            created_at=cls.convert_datetime(doc["created_at"]),
            updated_at=cls.convert_datetime(doc.get("updated_at", doc["created_at"])),
        )
