from fastapi import Depends
from sqlalchemy.orm import Session

from common.core.project.project_repository import ProjectRepository
from common.core.result.result_repository import ResultRepository
from common.infra.database import get_db
from common.infra.models.project import ProjectModel
from common.infra.models.result import ResultModel
from common.infra.repositories.project_repository import ProjectRepositoryImpl
from common.infra.repositories.result_repository import ResultRepositoryImpl


def get_project_repository(db: Session = Depends(get_db)) -> ProjectRepository:
    return ProjectRepositoryImpl(db)


def get_result_repository(db: Session = Depends(get_db)) -> ResultRepository:
    return ResultRepositoryImpl(db)
