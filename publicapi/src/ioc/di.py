from dependency_injector import containers, providers

from common.infra.repositories.project_repository import ProjectRepositoryImpl

class DIContainer(containers.DeclarativeContainer):
    project_repository = providers.Factory(ProjectRepositoryImpl)
