from typing import Union

from fastapi.responses import JSONResponse
from common.core.result.result import Result
from common.core.result.result_repository import ResultRepository
from fastapi import APIRouter, Depends, HTTPException, Header, Request

from resultsapi.src.domain.result.result_dto import ResultCreateDTO, ResultDTO
from resultsapi.src.domain.result.result_service import ResultService
from resultsapi.src.web.di.di import get_result_repository, get_result_service, get_version
from resultsapi.src.web.schemas.result_schema import ResultCreateSchema, ResultListResponseV1, ResultListResponseV2, ResultSchemaV1, ResultSchemaV2
result_api = APIRouter()

@result_api.post("/results", status_code=201)
def create_result(
    result: ResultCreateSchema,
    result_service: ResultService = Depends(get_result_service),
) -> ResultSchemaV1:
    result_dto = ResultCreateDTO(
        title=result.title,
        project_id=result.project_id
    )

    result: ResultDTO = result_service.create_result(result_dto)

    return ResultSchemaV1.from_dto(result)


@result_api.get(
    "/results",
    response_model=Union[ResultListResponseV1, ResultListResponseV2],
    openapi_extra={
        "parameters": [
            {
                "name": "accept",
                "in": "header",
                "required": True,
                "schema": {
                    "type": "string",
                    "default": "application/json; v=2",
                    "enum": ["application/json; v=1", "application/json; v=2"]
                }
            }
        ],
        "responses": {
            200: {
                "description": "Retrieve list of results",
                "content": {
                    "application/json; v=2": {
                        "schema": {
                            "$ref": "#/components/schemas/ResultListResponseV2"
                        }
                    },
                    "application/json; v=1": {
                        "schema": {
                            "$ref": "#/components/schemas/ResultListResponseV1"
                        }
                    }
                }
            }
        }
    }
)
def get_results(
    request: Request,
    result_service: ResultService = Depends(get_result_service)
):
    accept = request.headers.get("accept")
    results: list[ResultDTO] = result_service.get_all()
    version: str = "2"
    if "application/json;v=" in accept:
        version = accept.split("v=")[-1]
    if version == "1":
        data = ResultListResponseV1(results=[ResultSchemaV1.from_dto(result) for result in results])
        return JSONResponse(content=data.model_dump_json(), headers={"Content-Type": "application/json; v=1"})
    elif version == "2":
        data = ResultListResponseV2(results=[ResultSchemaV2.from_dto(result) for result in results])
        return JSONResponse(content=data.model_dump_json(), headers={"Content-Type": "application/json; v=2"})
    else:
        raise HTTPException(status_code=400, detail="Unsupported version")
