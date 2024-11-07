from fastapi import Depends, HTTPException, Header
from sqlalchemy.orm import Session

from common.core.project.project_repository import ProjectRepository
from common.core.result.result_repository import ResultRepository
from common.infra.database import get_db
from common.infra.repositories.project_repository import ProjectRepositoryImpl
from common.infra.repositories.result_repository import ResultRepositoryImpl
from resultsapi.src.domain.result.result_service import ResultService


def get_project_repository(db: Session = Depends(get_db)) -> ProjectRepository:
    return ProjectRepositoryImpl(db)


def get_result_repository(db: Session = Depends(get_db)) -> ResultRepository:
    return ResultRepositoryImpl(db)

def get_result_service(
    result_repository: ResultRepository = Depends(get_result_repository),
    project_repository: ProjectRepository = Depends(get_project_repository)
) -> ResultService:
    return ResultService(
        result_repository=result_repository,
        project_repository=project_repository
    )

def get_version(accept: str = Header(None)) -> str:
    if not accept:
        raise HTTPException(status_code=400, detail="Accept header missing")
    if "application/json;v=" in accept:
        version = accept.split("v=")[-1]
        return version
    else:
        raise HTTPException(status_code=400, detail="Version not specified in Accept header")

