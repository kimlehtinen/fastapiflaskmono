
from common.core.project.project import Project
from common.core.project.project_repository import ProjectRepository


class ProjectRepositoryImpl(ProjectRepository):
    def get_all(self) -> list[Project]:
        return [Project(1, 'Project 1'), Project(2, 'Project 2')]
