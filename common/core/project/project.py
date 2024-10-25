
from dataclasses import dataclass


@dataclass
class Project:
    id: int
    name: str

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name
        }
