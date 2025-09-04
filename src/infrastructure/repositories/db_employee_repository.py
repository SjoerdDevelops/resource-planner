from typing import List, Any
from application.interfaces import EmployeeRepository
from infrastructure.models import EmployeeModel
from domain.schemas import (
    EmployeeSchema,
    PersonalInfoSchema,
    EmploymentDetailsSchema,
    CompanyCredentialsSchema,
)


# TODO: Add @override method from typing when using python >3.12
class DBEmployeeRepository(EmployeeRepository):
    def get_by_id(self, id: int) -> Any:
        return EmployeeModel.get_or_none(EmployeeModel.id == id)

    def get_by_username(self, username: str) -> Any:
        return EmployeeModel.get_or_none(EmployeeModel.username == username)

    def add(
        self,
        personal: PersonalInfoSchema,
        employment: EmploymentDetailsSchema,
        credentials: CompanyCredentialsSchema,
    ) -> Any:
        employee = EmployeeModel.create(
            name=personal.name,
            surname=personal.surname,
            fte=employment.fte,
            utilization_rate=employment.utilization_rate,
            username=credentials.username,
            acronym=credentials.acronym,
        )
        return employee

    def delete(self, id: int):
        EmployeeModel.delete_by_id(id)

    def update(self, employee: EmployeeSchema) -> Any:
        EmployeeModel.update(
            name=employee.personal.name,
            surname=employee.personal.surname,
            fte=employee.employment.fte,
            utilization_rate=employee.employment.utilization_rate,
            username=employee.credentials.username,
            acronym=employee.credentials.acronym,
        ).where(EmployeeModel.id == employee.id).execute()

        return self.get_by_id(employee.id)

    def list_all(self) -> List[Any]:
        return list(EmployeeModel.select())
