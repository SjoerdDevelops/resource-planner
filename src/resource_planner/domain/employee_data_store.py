from abc import ABC, abstractmethod
from typing import List, Optional
from resource_planner.domain.employee import Employee


class EmployeeDataStore(ABC):
    @abstractmethod
    def get_by_id(self, id: int) -> Optional[Employee]:
        pass

    @abstractmethod
    def add(self, employee: Employee) -> Employee:
        pass

    @abstractmethod
    def update(self, username: str, employee: Employee) -> int:
        pass

    @abstractmethod
    def list_all(self) -> List[Employee]:
        pass
