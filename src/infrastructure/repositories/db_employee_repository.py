from typing import Optional, Any
from application.interfaces import EmployeeRepository
from infrastructure.models import EmployeeModel
from domain.schemas import EmployeeModelSchema
from domain.entities import (
    Employee,
    PersonalInfo,
    EmploymentDetails,
    CompanyCredentials,
)
from uuid import UUID


# TODO: Add @override method from typing when using python >3.12
class DBEmployeeRepository(EmployeeRepository):
    def find_by_id(self, id: UUID) -> Optional[Employee]:
        result = EmployeeModel.get_or_none(EmployeeModel.id == id)
        return validate_or_none(result)

    def find_by_username(self, username: str) -> Optional[Employee]:
        result = EmployeeModel.get_or_none(EmployeeModel.username == username)
        return validate_or_none(result)

    def find_by_acronym(self, acronym: str) -> Optional[Employee]:
        result = EmployeeModel.get_or_none(EmployeeModel.acronym == acronym)
        return validate_or_none(result)

    def add(self, employee: Employee) -> Optional[Employee]:
        result = EmployeeModel.create(
            id=employee.id,
            name=employee.personal.name,
            surname=employee.personal.surname,
            fte=employee.employment.fte,
            utilization_rate=employee.employment.utilization_rate,
            username=employee.credentials.username,
            acronym=employee.credentials.acronym,
        )
        return validate_or_none(result)

    def remove(self, id: UUID):
        EmployeeModel.delete_by_id(id)

    def update(self, employee: Employee) -> Optional[Employee]:
        EmployeeModel.update(
            name=employee.personal.name,
            surname=employee.personal.surname,
            fte=employee.employment.fte,
            utilization_rate=employee.employment.utilization_rate,
            username=employee.credentials.username,
            acronym=employee.credentials.acronym,
        ).where(EmployeeModel.id == employee.id).execute()

        result = self.find_by_id(employee.id)
        return validate_or_none(result)

    def list_all(self) -> list[Employee]:
        return [
            to_employee(EmployeeModelSchema.model_validate(result))
            for result in EmployeeModel.select()
        ]


def to_employee(model: EmployeeModelSchema) -> Employee:
    return Employee(
        model.id,
        PersonalInfo(model.name, model.username),
        EmploymentDetails(model.fte, model.utilization_rate),
        CompanyCredentials(model.username, model.acronym),
    )


def validate_or_none(data: Any) -> Optional[Employee]:
    if data:
        employee_schema = EmployeeModelSchema.model_validate(data)
        return to_employee(employee_schema)
    else:
        return None
