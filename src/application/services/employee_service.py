from uuid import uuid4, UUID
from application.interfaces import EmployeeRepository
from domain.entities import (
    Employee,
    PersonalInfo,
    EmploymentDetails,
    CompanyCredentials,
)


class EmployeeService:
    def __init__(self, repository: EmployeeRepository) -> None:
        self._repository: EmployeeRepository = repository
        self._employees: list[Employee] = self.list_all()

    def add(
        self,
        personal: PersonalInfo,
        employment: EmploymentDetails,
        credentials: CompanyCredentials,
    ) -> Employee:
        for employee in self._employees:
            if self.find_by_username(credentials.username):
                raise ValueError(
                    f"An employee with username {credentials.username} already exists"
                )

            if self.find_by_acronym(credentials.acronym):
                raise ValueError(
                    f"An employee with acronym {credentials.acronym} already exists"
                )

        employee = Employee(uuid4(), personal, employment, credentials)
        _ = self._repository.add(employee)
        return employee

    def remove(self, id: UUID) -> None:
        self._repository.remove(id)

    def find_by_id(self, id: UUID) -> Employee | None:
        return self._repository.find_by_id(id)

    def find_by_username(self, username: str) -> Employee | None:
        return self._repository.find_by_username(username)

    def find_by_acronym(self, acronym: str) -> Employee | None:
        return self._repository.find_by_acronym(acronym)

    def list_all(self) -> list[Employee]:
        return self._repository.list_all()
