
from dataclasses import dataclass


@dataclass
class Project:
    title: str
    id: int | None = None

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title
        }
