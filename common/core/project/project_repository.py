
from abc import ABC, abstractmethod
from common.core.project.project import Project


class ProjectRepository(ABC):
    @abstractmethod
    def create(self, project: Project) -> Project:
        pass

    @abstractmethod
    def get_all(self) -> list[Project]:
        pass

    @abstractmethod
    def get_by_id(self, id: int) -> Project:
        pass
