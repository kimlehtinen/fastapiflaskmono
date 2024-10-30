from common.core.project.project_repository import ProjectRepository
from common.core.result.result import Result
from common.core.result.result_repository import ResultRepository
from fastapi import APIRouter, Depends

from resultsapi.src.web.di.di import get_project_repository, get_result_repository
from resultsapi.src.web.schemas.result import ResultCreateSchema

result_api = APIRouter()

@result_api.post("/results")
def create_result(
    result: ResultCreateSchema,
    result_repository: ResultRepository = Depends(get_result_repository),
    project_repository: ProjectRepository = Depends(get_project_repository)
):
    project = project_repository.get_by_id(result.project_id)
    if not project:
        return {"message": "Project not found"}, 404
    new_result = Result(
        title=result.title,
        project=project
    )
    return result_repository.create(new_result)

@result_api.get("/results")
def get_results(result_repository: ResultRepository = Depends(get_result_repository)):
    return result_repository.get_all()
