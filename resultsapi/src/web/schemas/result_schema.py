
from pydantic import BaseModel

from common.core.project.project import Project
from common.core.result.result import Result
from resultsapi.src.domain.result.result_dto import ResultDTO

class ProjectSchema(BaseModel):
    id: int
    title: str

    @classmethod
    def from_domain(cls, project: Project) -> 'ProjectSchema':
        return cls(
            id=project.id,
            title=project.title
        )


class ResultCreateSchema(BaseModel):
    title: str
    project_id: int


class ResultSchemaV1(BaseModel):
    title: str
    project: ProjectSchema

    @classmethod
    def from_dto(cls, result: ResultDTO) -> 'ResultSchemaV1':
        return cls(
            name=result.title,
            project=ProjectSchema.from_domain(result.project)
        )

    @classmethod
    def from_domain(cls, result: Result) -> 'ResultSchemaV1':
        return cls(
            name=result.title,
            project=ProjectSchema.from_domain(result.project)
        )
    
class ResultSchemaV2(BaseModel):
    name: str
    project: ProjectSchema

    @classmethod
    def from_dto(cls, result: ResultDTO) -> 'ResultSchemaV1':
        return cls(
            title=result.title,
            project=ProjectSchema.from_domain(result.project)
        )

    @classmethod
    def from_domain(cls, result: Result) -> 'ResultSchemaV1':
        return cls(
            name=result.title,
            project=ProjectSchema.from_domain(result.project)
        )


class ResultListResponseV1(BaseModel):
    results: list[ResultSchemaV1]


class ResultListResponseV2(BaseModel):
    results: list[ResultSchemaV2]
    prev: str
    next: str
