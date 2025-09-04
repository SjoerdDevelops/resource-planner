from pydantic import BaseModel


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
    id: int
    personal: PersonalInfoSchema
    employment: EmploymentDetailsSchema
    credentials: CompanyCredentialsSchema
