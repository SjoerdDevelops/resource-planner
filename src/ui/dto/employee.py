from dataclasses import dataclass
from uuid import UUID


@dataclass
class PersonalInfoDTO:
    name: str
    surname: str


@dataclass
class EmploymentDetailsDTO:
    fte: float
    utilization_rate: float


@dataclass
class CompanyCredentialsDTO:
    username: str
    acronym: str


@dataclass
class EmployeeDTO:
    id: UUID
    personal: PersonalInfoDTO
    employment: EmploymentDetailsDTO
    credentials: CompanyCredentialsDTO
