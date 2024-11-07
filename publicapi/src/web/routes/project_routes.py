
from flask import Blueprint, jsonify, request
from dependency_injector.wiring import inject, Provide

from common.core.project.project import Project
from publicapi.src.domain.project.project_dto import ProjectCreateDTO, ProjectDTO
from publicapi.src.domain.project.project_service import ProjectService
from publicapi.src.ioc.di import DIContainer
from publicapi.src.web.schemas.project_schema import ProjectCreateSchema


projects_api = Blueprint('projects_api', __name__)

@projects_api.route('/projects', methods=['POST'])
@inject
def create_project(
    project_service: ProjectService = Provide[DIContainer.project_service]
):
    data = ProjectCreateSchema().load(request.json)
    project = ProjectCreateDTO(**data)
    project: ProjectDTO = project_service.create_project(project)

    return jsonify(project.to_dict()), 201

@projects_api.route('/projects', methods=['GET'])
@inject
def get_projects(
    project_service: ProjectService = Provide[DIContainer.project_service]
):
    projects: list[Project] = project_service.get_all()

    return jsonify([project.to_dict() for project in projects])
