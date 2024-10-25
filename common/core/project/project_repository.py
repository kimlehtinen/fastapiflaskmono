
from abc import ABC, abstractmethod
from common.core.project.project import Project


class ProjectRepository(ABC):
    @abstractmethod
    def get_all(self) -> list[Project]:
        pass
        
