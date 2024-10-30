from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from common.core.result.result import Result
from common.infra.database import Base

class ResultModel(Base):
    __tablename__ = 'results'

    id = Column(Integer, primary_key=True)
    title = Column(String(50))
    project_id = Column(Integer, ForeignKey('projects.id'))
    project = relationship('ProjectModel', back_populates='results')

    def to_domain(self) -> Result:
        project_domain = self.project.to_domain() if self.project else None
        return Result(id=self.id, title=self.title, project=project_domain)
