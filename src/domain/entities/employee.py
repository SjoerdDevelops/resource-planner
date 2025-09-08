from dataclasses import dataclass
from uuid import UUID, uuid4


@dataclass
class PersonalInfo:
    name: str
    surname: str


@dataclass
class EmploymentDetails:
    fte: float
    utilization_rate: float


@dataclass
class CompanyCredentials:
    username: str
    acronym: str


@dataclass
class Employee:
    id: UUID
    personal: PersonalInfo
    employment: EmploymentDetails
    credentials: CompanyCredentials

    @property
    def utilization_percentage(self):
        return self.employment.utilization_rate * 100
