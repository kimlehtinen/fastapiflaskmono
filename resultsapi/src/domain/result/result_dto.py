from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from common.core.project.project import Project
    from common.core.result.result import Result


@dataclass
class ResultCreateDTO:
    title: str
    project_id: int


@dataclass
class ResultDTO:
    title: str
    project: 'Project'

    @classmethod
    def from_domain(cls, result: 'Result') -> 'ResultDTO':
        return cls(
            title=result.title,
            project=result.project.to_dict()
        )
