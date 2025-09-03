from typing import List, Optional
from domain.entities.employee import Employee
from domain.interfaces.employee_repository import EmployeeRepository
from infrastructure.models.employee_model import EmployeeModel
from infrastructure.schemas.employee_schema import (
    create_employee_from_data,
    create_employee_from_schema,
)


# TODO: Add @override method from typing when using python >3.12
class DBEmployeeRepository(EmployeeRepository):
    def get_by_id(self, id: int) -> Optional[Employee]:
        row = EmployeeModel.get_or_none(EmployeeModel.id == id)
        return create_employee_from_data(row)

    def add(self, employee: Employee) -> Employee:
        row = EmployeeModel.create(
            name=employee.personal.name,
            surname=employee.personal.surname,
            fte=employee.employment.fte,
            utilization_rate=employee.employment.utilization_rate,
            username=employee.credentials.username,
            acronym=employee.credentials.acronym,
        )
        return create_employee_from_schema(row)

    def update(self, username: str, employee: Employee) -> int:
        query = EmployeeModel.update(
            name=employee.personal.name,
            surname=employee.personal.surname,
            fte=employee.employment.fte,
            utilization_rate=employee.employment.utilization_rate,
            username=employee.credentials.username,
            acronym=employee.credentials.acronym,
        ).where(EmployeeModel.username == username)

        rows_modified = query.execute()
        return rows_modified

    def list_all(self) -> List[Employee]:
        return [
            employee
            for row in EmployeeModel.select()
            if (employee := create_employee_from_data(row)) is not None
        ]
