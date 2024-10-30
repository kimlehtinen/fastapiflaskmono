from dependency_injector import containers, providers

from common.infra.repositories.project_repository import ProjectRepositoryImpl
from common.infra.database import get_db

class DIContainer(containers.DeclarativeContainer):
    db = providers.Resource(get_db)
    project_repository = providers.Factory(ProjectRepositoryImpl, db=db)
