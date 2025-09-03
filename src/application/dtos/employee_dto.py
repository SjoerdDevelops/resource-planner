from pydantic import BaseModel, ConfigDict, ValidationError
from typing import Any, Optional


class EmployeeDTO(BaseModel):
    id: int
    name: str
    surname: str
    fte: float
    utilization_rate: float
    username: str
    acronym: str

    model_config = ConfigDict(from_attributes=True)


def validate_employee(data: Any) -> Optional[EmployeeDTO]:
    try:
        employeeDTO: EmployeeDTO = EmployeeDTO.model_validate(data)
        return employeeDTO
    except ValidationError as e:
        print("Validation failed:", e.json())
        return None
