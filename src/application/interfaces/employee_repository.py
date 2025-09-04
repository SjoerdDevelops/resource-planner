from abc import ABC, abstractmethod
from typing import List, Any
from domain.schemas import (
    EmployeeSchema,
    PersonalInfoSchema,
    EmploymentDetailsSchema,
    CompanyCredentialsSchema,
)


class EmployeeRepository(ABC):
    @abstractmethod
    def get_by_id(self, id: int) -> Any:
        pass

    @abstractmethod
    def get_by_username(self, username: str) -> Any:
        pass

    @abstractmethod
    def add(
        self,
        personal: PersonalInfoSchema,
        employment: EmploymentDetailsSchema,
        credentials: CompanyCredentialsSchema,
    ) -> Any:
        pass

    @abstractmethod
    def delete(self, id: int):
        pass

    @abstractmethod
    def update(self, employee: EmployeeSchema) -> Any:
        pass

    @abstractmethod
    def list_all(self) -> List[Any]:
        pass
