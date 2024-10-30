
from unittest.mock import MagicMock
import pytest

from common.core.project.project import Project
from common.core.project.project_repository import ProjectRepository
from publicapi.src.domain.project.project_dto import ProjectCreateDTO
from publicapi.src.domain.project.project_service import ProjectService


@pytest.fixture
def project_repository() -> ProjectRepository:
    repo = MagicMock()
    repo.create.side_effect = _persist

    return repo


@pytest.fixture
def sut(project_repository) -> ProjectService:
    return ProjectService(project_repository=project_repository)


def test_create_project(sut: ProjectService):
    project_dto = ProjectCreateDTO(title='Project 1')
    
    project: Project = sut.create_project(project_dto)

    assert project.title == 'Project 1'


def _persist(item):
    return item
