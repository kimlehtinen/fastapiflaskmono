
from common.core.project.project import Project
from common.core.project.project_repository import ProjectRepository
from publicapi.src.domain.project.project_dto import ProjectCreateDTO


class ProjectService:
    _project_repository: ProjectRepository

    def __init__(self, project_repository: ProjectRepository):
        self._project_repository = project_repository

    def create_project(self, project_dto: ProjectCreateDTO) -> dict:
        project = Project(title=project_dto.title)

        return self._project_repository.create(project)
