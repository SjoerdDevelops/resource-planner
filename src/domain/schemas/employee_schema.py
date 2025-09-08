from pydantic import BaseModel
from uuid import UUID


class PersonalInfoSchema(BaseModel):
    name: str
    surname: str


class EmploymentDetailsSchema(BaseModel):
    fte: float
    utilization_rate: float


class CompanyCredentialsSchema(BaseModel):
    username: str
    acronym: str


class EmployeeSchema(BaseModel):
    id: UUID
    personal: PersonalInfoSchema
    employment: EmploymentDetailsSchema
    credentials: CompanyCredentialsSchema
