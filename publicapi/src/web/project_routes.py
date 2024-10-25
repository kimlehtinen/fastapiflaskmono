
from flask import Blueprint, jsonify
from dependency_injector.wiring import inject, Provide

from common.core.project.project import Project
from common.core.project.project_repository import ProjectRepository
from publicapi.src.ioc.di import DIContainer


projects_api = Blueprint('projects_api', __name__)

@projects_api.route('/projects', methods=['GET'])
@inject
def get_projects(
    project_repository: ProjectRepository = Provide[DIContainer.project_repository]
):
    projects: list[Project] = project_repository.get_all()

    return jsonify([project.to_dict() for project in projects])
