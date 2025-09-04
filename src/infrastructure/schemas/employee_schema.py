from pydantic import BaseModel, ConfigDict, ValidationError
from typing import Any, Optional
from domain.entities import (
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
        employee_schema: EmployeeSchema = EmployeeSchema.model_validate(data)
        return employee_schema
    except ValidationError as e:
        print("Validation failed:", e.json())
        return None


def create_employee_from_schema(employee_schema: EmployeeSchema) -> Employee:
    return Employee(
        PersonalInfo(employee_schema.name, employee_schema.surname),
        EmploymentDetails(employee_schema.fte, employee_schema.utilization_rate),
        CompanyCredentials(employee_schema.username, employee_schema.acronym),
    )


def create_employee_from_data(data: Any) -> Optional[Employee]:
    validated_employee = validate_employee(data)
    if validated_employee is None:
        return None

    return create_employee_from_schema(validated_employee)
