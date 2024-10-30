from sqlalchemy.orm import Session

from common.core.project.project import Project
from common.core.project.project_repository import ProjectRepository
from common.infra.models.project import ProjectModel


class ProjectRepositoryImpl(ProjectRepository):
    def __init__(self, db: Session):
        self.db = db

    def create(self, project: Project) -> Project:
        project_db = ProjectModel(title=project.title)
        self.db.add(project_db)
        self.db.commit()

        return project_db.to_domain()

    def get_all(self) -> list[Project]:
        projects_db: list[ProjectModel] = self.db.query(ProjectModel).all()
        return [project.to_domain() for project in projects_db]
    
    def get_by_id(self, id: int) -> Project:
        project_db = self.db.query(ProjectModel).filter(ProjectModel.id == id).first()
        return project_db.to_domain() if project_db else None
