from abc import ABC, abstractmethod
from typing import Optional
from domain.entities import Employee
from uuid import UUID


class EmployeeRepository(ABC):
    @abstractmethod
    def find_by_id(self, id: UUID) -> Optional[Employee]:
        pass

    @abstractmethod
    def find_by_username(self, username: str) -> Optional[Employee]:
        pass

    @abstractmethod
    def find_by_acronym(self, acronym: str) -> Optional[Employee]:
        pass

    @abstractmethod
    def add(self, employee: Employee) -> Optional[Employee]:
        pass

    @abstractmethod
    def remove(self, id: UUID):
        pass

    @abstractmethod
    def update(self, employee: Employee) -> Optional[Employee]:
        pass

    @abstractmethod
    def list_all(self) -> list[Employee]:
        pass
