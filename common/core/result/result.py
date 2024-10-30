
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from common.core.project.project import Project


@dataclass
class Result:
    title: str
    project: 'Project'
    id: int | None = None

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'project': self.project.to_dict() if self.project else None
        }
