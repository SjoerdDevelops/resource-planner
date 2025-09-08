from application.services import EmployeeService
from domain.entities import (
    Employee,
    PersonalInfo,
    EmploymentDetails,
    CompanyCredentials,
)
from ui.contexts import employee_context
from ui.dto import (
    EmployeeDTO,
    PersonalInfoDTO,
    EmploymentDetailsDTO,
    CompanyCredentialsDTO,
)
from uuid import UUID


class EmployeeController:
    def __init__(self, employee_service: EmployeeService):
        self._employee_service = employee_service
        self.update_context()

        employee_context.add_employee_requested.connect(self.on_add_employee_requested)
        employee_context.remove_employee_requested.connect(
            self.on_remove_employee_requested
        )

    def on_add_employee_requested(
        self,
        personal_dto: PersonalInfoDTO,
        employment_dto: EmploymentDetailsDTO,
        credentials_dto: CompanyCredentialsDTO,
    ):
        try:
            employee = self._employee_service.add(
                to_personal_info(personal_dto),
                to_employment_details(employment_dto),
                to_company_credentials(credentials_dto),
            )
            employee_context.add_employee(to_employee_dto(employee))

        except Exception as e:
            employee_context.error_occured.emit(e)

    def on_remove_employee_requested(self, id: UUID):
        try:
            self._employee_service.remove(id)
            employee_context.remove_employee(id)
        except Exception as e:
            employee_context.error_occured.emit(e)

    def update_context(self):
        employees = self._employee_service.list_all()
        employees_dto = [to_employee_dto(employee) for employee in employees]
        employee_context.reset(employees_dto)


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
    return PersonalInfoDTO(personal.name, personal.surname)


def to_employment_details_dto(employment: EmploymentDetails) -> EmploymentDetailsDTO:
    return EmploymentDetailsDTO(employment.fte, employment.utilization_rate)


def to_company_credentials_dto(
    credentials: CompanyCredentials,
) -> CompanyCredentialsDTO:
    return CompanyCredentialsDTO(credentials.username, credentials.acronym)


def to_employee_dto(employee: Employee) -> EmployeeDTO:
    return EmployeeDTO(
        employee.id,
        to_personal_info_dto(employee.personal),
        to_employment_details_dto(employee.employment),
        to_company_credentials_dto(employee.credentials),
    )
