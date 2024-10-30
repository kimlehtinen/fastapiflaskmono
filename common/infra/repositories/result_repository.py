from sqlalchemy.orm import Session

from common.core.result.result import Result
from common.core.result.result_repository import ResultRepository
from common.infra.models.project import ProjectModel
from common.infra.models.result import ResultModel


class ResultRepositoryImpl(ResultRepository):
    def __init__(self, db: Session):
        self.db = db

    def create(self, result: Result) -> Result:
        project_db = self.db.query(ProjectModel).filter(ProjectModel.id == result.project.id).first()
        result_db = ResultModel(title=result.title, project=project_db)
        self.db.add(result_db)
        self.db.commit()

        return result_db.to_domain()

    def get_all(self) -> list[Result]:
        results_db: list[ResultModel] = self.db.query(ResultModel).all()

        return [result_db.to_domain() for result_db in results_db]
