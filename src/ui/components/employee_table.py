from typing import Tuple, Callable, Any, List
from PySide6.QtWidgets import QTableWidget, QTableWidgetItem
from domain.entities import Employee
from application.services import EmployeeService
from infrastructure.repositories import DBEmployeeRepository

# Column = (header label, extractor function)
Column = Tuple[str, Callable[[Employee], Any]]


class EmployeeTable(QTableWidget):
    def __init__(self):
        super().__init__()

        repository = DBEmployeeRepository()
        service = EmployeeService(repository)

        self.employees = service.list_all()

        self.columns: List[Column] = [
            ("Name", lambda employee: employee.personal.name),
            ("Surname", lambda employee: employee.personal.surname),
            ("Username", lambda employee: employee.credentials.username),
            ("Acronym", lambda employee: employee.credentials.acronym),
            ("FTE", lambda employee: employee.employment.fte),
            ("Utilization Rate", lambda employee: employee.employment.utilization_rate),
        ]

        self.setColumnCount(len(self.columns))
        self.setHorizontalHeaderLabels([label for (label, _) in self.columns])
        self.update_table(self.employees)

    def update_table(self, employees: List[Employee]):
        self.employees = employees
        self.setRowCount(len(self.employees))

        for row, employee in enumerate(self.employees):
            for col, (_, extractor) in enumerate(self.columns):
                value: Any = extractor(employee)
                self.setItem(row, col, QTableWidgetItem(str(value)))
