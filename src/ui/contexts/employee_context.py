from PySide6.QtCore import QObject, Signal
from ui.dto import (
    EmployeeDTO,
    PersonalInfoDTO,
    EmploymentDetailsDTO,
    CompanyCredentialsDTO,
)
from uuid import UUID


class _EmployeeContext(QObject):
    add_employee_requested = Signal(
        PersonalInfoDTO, EmploymentDetailsDTO, CompanyCredentialsDTO
    )
    remove_employee_requested = Signal(UUID)
    update_employee_requested = Signal(EmployeeDTO)

    employee_added = Signal()
    employee_removed = Signal()
    data_changed = Signal()

    error_occured = Signal(str)

    def __init__(self):
        super().__init__()
        self._employees: list[EmployeeDTO] = []

    def reset(self, employees: list[EmployeeDTO]):
        self._employees = employees
        self.data_changed.emit()

    def add_employee(self, employee: EmployeeDTO):
        self._employees.append(employee)
        self.employee_added.emit()
        self.data_changed.emit()

    def remove_employee(self, id: UUID):
        employee = next(
            (employee for employee in self._employees if employee.id == id), None
        )
        if employee:
            self._employees.remove(employee)
        self.employee_removed.emit()
        self.data_changed.emit()

    def list_all(self) -> list[EmployeeDTO]:
        # Return a copy to prevent list mutation from the outside
        return list(self._employees)


employee_context = _EmployeeContext()
