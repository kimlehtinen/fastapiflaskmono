
from common.core.project.project import Project
from common.core.project.project_repository import ProjectRepository
from publicapi.src.domain.project.project_dto import ProjectCreateDTO, ProjectDTO


class ProjectService:
    _project_repository: ProjectRepository

    def __init__(self, project_repository: ProjectRepository):
        self._project_repository = project_repository

    def create_project(self, project_dto: ProjectCreateDTO) -> ProjectDTO:
        project = Project(title=project_dto.title)

        project = self._project_repository.create(project)

        return project.to_dto()
    
    def get_all(self) -> list[ProjectDTO]:
        projects = self._project_repository.get_all()

        return [project.to_dto() for project in projects]
