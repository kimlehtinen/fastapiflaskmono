from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from common.core.project.project import Project
from common.infra.database import Base

class ProjectModel(Base):
    __tablename__ = 'projects'

    id = Column(Integer, primary_key=True)
    title = Column(String(50))
    results = relationship('ResultModel', back_populates='project')

    def to_domain(self) -> Project:
        return Project(
            id=self.id,
            title=self.title,
        )
