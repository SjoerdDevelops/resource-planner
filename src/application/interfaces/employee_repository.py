from abc import ABC, abstractmethod
from domain.entities import Employee
from uuid import UUID


class EmployeeRepository(ABC):
    @abstractmethod
    def find_by_id(self, id: UUID) -> Employee | None:
        pass

    @abstractmethod
    def find_by_username(self, username: str) -> Employee | None:
        pass

    @abstractmethod
    def find_by_acronym(self, acronym: str) -> Employee | None:
        pass

    @abstractmethod
    def add(self, employee: Employee) -> Employee | None:
        pass

    @abstractmethod
    def remove(self, id: UUID) -> None:
        pass

    @abstractmethod
    def update(self, employee: Employee) -> Employee | None:
        pass

    @abstractmethod
    def list_all(self) -> list[Employee]:
        pass
