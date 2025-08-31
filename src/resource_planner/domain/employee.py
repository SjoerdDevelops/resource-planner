from dataclasses import dataclass


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
    personal: PersonalInfo
    employment: EmploymentDetails
    credentials: CompanyCredentials


sjoerd = Employee(
    PersonalInfo("Sjoerd", "Kuitert"),
    EmploymentDetails(1.0, 0.8),
    CompanyCredentials("kuiters", "SKT"),
)
