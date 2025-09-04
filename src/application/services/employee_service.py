from typing import Optional, Any, List
from application.interfaces import EmployeeRepository
from domain.entities import (
    Employee,
    PersonalInfo,
    EmploymentDetails,
    CompanyCredentials,
)
from domain.schemas import (
    EmployeeFlatDataSchema,
    PersonalInfoSchema,
    EmploymentDetailsSchema,
    CompanyCredentialsSchema,
)


def create_employee(employee: EmployeeFlatDataSchema) -> Employee:
    return Employee(
        employee.id,
        PersonalInfo(employee.name, employee.surname),
        EmploymentDetails(employee.fte, employee.utilization_rate),
        CompanyCredentials(employee.username, employee.acronym),
    )


class EmployeeService:
    def __init__(self, repository: EmployeeRepository):
        self.repository = repository

    # TODO: Try to add, if it fails, catch the error
    def add_employee(
        self,
        personal: PersonalInfo,
        employment: EmploymentDetails,
        credentials: CompanyCredentials,
    ) -> Optional[Employee]:
        existing: Optional[dict[str, Any]] = self.repository.get_by_username(
            credentials.username
        )

        if existing:
            raise ValueError(
                f"There is already a user with username {credentials.username}."
            )

        result: Any = self.repository.add(
            PersonalInfoSchema(**personal.__dict__),
            EmploymentDetailsSchema(**employment.__dict__),
            CompanyCredentialsSchema(**credentials.__dict__),
        )

        employee = EmployeeFlatDataSchema.model_validate(result)

        return create_employee(employee)

    # TODO: Perhaps this should be done using the userid
    def delete_employee(self, id: int):
        self.repository.delete(id)

    def list_all(self) -> List[Employee]:
        result_list: List[Any] = self.repository.list_all()

        employees = [
            EmployeeFlatDataSchema.model_validate(result) for result in result_list
        ]

        return [create_employee(employee) for employee in employees]
