
from dataclasses import dataclass
from typing import TYPE_CHECKING

from resultsapi.src.domain.result.result_dto import ResultDTO

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
    
    def to_dto(self):
        return ResultDTO(
            title=self.title,
            project=self.project
        )
