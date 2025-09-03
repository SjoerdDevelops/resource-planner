from pydantic import BaseModel, ConfigDict, ValidationError
from typing import Any, Optional
from domain.entities.employee import (
    Employee,
    PersonalInfo,
    EmploymentDetails,
    CompanyCredentials,
)


class EmployeeSchema(BaseModel):
    id: int
    name: str
    surname: str
    fte: float
    utilization_rate: float
    username: str
    acronym: str

    model_config = ConfigDict(from_attributes=True)


def validate_employee(data: Any) -> Optional[EmployeeSchema]:
    try:
        employeeDTO: EmployeeSchema = EmployeeSchema.model_validate(data)
        return employeeDTO
    except ValidationError as e:
        print("Validation failed:", e.json())
        return None


def create_employee_from_schema(employeeDTO: EmployeeSchema) -> Employee:
    return Employee(
        PersonalInfo(employeeDTO.name, employeeDTO.surname),
        EmploymentDetails(employeeDTO.fte, employeeDTO.utilization_rate),
        CompanyCredentials(employeeDTO.username, employeeDTO.acronym),
    )


def create_employee_from_data(data: Any) -> Optional[Employee]:
    validated_employee = validate_employee(data)
    if validated_employee is None:
        return None

    return create_employee_from_schema(validated_employee)
