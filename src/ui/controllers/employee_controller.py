from application.services import EmployeeService
from domain.entities import (
    Employee,
    PersonalInfo,
    EmploymentDetails,
    CompanyCredentials,
)
from ui.dto import (
    EmployeeDTO,
    PersonalInfoDTO,
    EmploymentDetailsDTO,
    CompanyCredentialsDTO,
)
from uuid import UUID
from PySide6.QtCore import QObject


class EmployeeController(QObject):
    def __init__(self, employee_service: EmployeeService) -> None:
        super().__init__()
        self._employee_service: EmployeeService = employee_service

    def add_employee(
        self,
        personal_dto: PersonalInfoDTO,
        employment_dto: EmploymentDetailsDTO,
        credentials_dto: CompanyCredentialsDTO,
    ) -> None:
        _ = self._employee_service.add(
            to_personal_info(personal_dto),
            to_employment_details(employment_dto),
            to_company_credentials(credentials_dto),
        )

    def remove_employee(self, id: UUID) -> None:
        self._employee_service.remove(id)

    def list_employees(self) -> list[EmployeeDTO]:
        employees = self._employee_service.list_all()
        employees_dto = [to_employee_dto(employee) for employee in employees]
        return employees_dto


class EmployeeControllerFactory:
    def __init__(self, employee_service: EmployeeService) -> None:
        self._employee_service: EmployeeService = employee_service

    def create(self) -> EmployeeController:
        return EmployeeController(self._employee_service)


def to_personal_info(personal: PersonalInfoDTO) -> PersonalInfo:
    return PersonalInfo(personal.name, personal.surname)


def to_employment_details(employment: EmploymentDetailsDTO) -> EmploymentDetails:
    return EmploymentDetails(employment.fte, employment.utilization_rate)


def to_company_credentials(credentials: CompanyCredentialsDTO) -> CompanyCredentials:
    return CompanyCredentials(credentials.username, credentials.acronym)


def to_employee(employee: EmployeeDTO) -> Employee:
    return Employee(
        employee.id,
        to_personal_info(employee.personal),
        to_employment_details(employee.employment),
        to_company_credentials(employee.credentials),
    )


def to_personal_info_dto(personal: PersonalInfo) -> PersonalInfoDTO:
    return PersonalInfoDTO(name=personal.name, surname=personal.surname)


def to_employment_details_dto(employment: EmploymentDetails) -> EmploymentDetailsDTO:
    return EmploymentDetailsDTO(
        fte=employment.fte, utilization_rate=employment.utilization_rate
    )


def to_company_credentials_dto(
    credentials: CompanyCredentials,
) -> CompanyCredentialsDTO:
    return CompanyCredentialsDTO(
        username=credentials.username, acronym=credentials.acronym
    )


def to_employee_dto(employee: Employee) -> EmployeeDTO:
    return EmployeeDTO(
        id=employee.id,
        personal=to_personal_info_dto(employee.personal),
        employment=to_employment_details_dto(employee.employment),
        credentials=to_company_credentials_dto(employee.credentials),
    )
