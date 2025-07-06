from abc import ABC, abstractmethod
from typing import Any, TypeVar, Generic

T = TypeVar('T')

class UseCaseResult(Generic[T]):

    def __init__(self, result: T, error: Exception | None = None):
        self._result = result
        self._error = error

    def result(self) -> T:
        return self._result
    
    def is_error(self) -> bool:
        return self._error != None

    def error(self) -> Exception | None:
        return self._error


class UseCase(ABC):

    @abstractmethod
    def execute(self) -> UseCaseResult:
        pass