
from dataclasses import dataclass

from publicapi.src.domain.project.project_dto import ProjectDTO


@dataclass
class Project:
    title: str
    id: int | None = None

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title
        }
    
    def to_dto(self):
        return ProjectDTO(
            id=self.id,
            title=self.title
        )
