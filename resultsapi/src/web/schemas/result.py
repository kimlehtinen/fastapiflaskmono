
from pydantic import BaseModel, Field


class ResultCreateSchema(BaseModel):
    title: str
    project_id: int
