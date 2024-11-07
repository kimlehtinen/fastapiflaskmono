from common.core.project.project_repository import ProjectRepository
from common.core.result.result import Result
from common.core.result.result_repository import ResultRepository
from resultsapi.src.domain.result.result_dto import ResultCreateDTO, ResultDTO


class ResultService:
    _result_repository: ResultRepository
    _project_repository: ProjectRepository

    def __init__(
        self,
        result_repository: ResultRepository,
        project_repository: ProjectRepository
    ):
        self._result_repository = result_repository
        self._project_repository = project_repository

    def create_result(self, result_dto: ResultCreateDTO) -> ResultDTO:
        result = Result(
            title=result_dto.title,
            project=self._project_repository.get_by_id(result_dto.project_id)
        )

        result = self._result_repository.create(result)

        return result.to_dto()
    
    def get_all(self) -> list[ResultDTO]:
        results = self._result_repository.get_all()

        return [result.to_dto() for result in results]
