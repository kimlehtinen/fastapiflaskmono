
from abc import ABC, abstractmethod

from common.core.result.result import Result


class ResultRepository(ABC):
    @abstractmethod
    def create(self, result: Result) -> Result:
        pass

    @abstractmethod
    def get_all(self) -> list[Result]:
        pass
