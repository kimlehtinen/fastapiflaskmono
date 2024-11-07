from dataclasses import dataclass


@dataclass
class ProjectCreateDTO:
    title: str


@dataclass
class ProjectDTO:
    id: int
    title: str

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title
        }
