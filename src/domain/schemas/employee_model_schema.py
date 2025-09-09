from pydantic import BaseModel, ConfigDict
from uuid import UUID


class EmployeeModelSchema(BaseModel):
    id: UUID
    name: str
    surname: str
    fte: float
    utilization_rate: float
    username: str
    acronym: str

    model_config: ConfigDict = ConfigDict(from_attributes=True)
