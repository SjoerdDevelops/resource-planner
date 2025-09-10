from typing import Callable, TypeAlias
from PySide6.QtWidgets import QTableWidget, QTableWidgetItem
from ui.dto import EmployeeDTO

# Column = (header label, extractor function)
Column: TypeAlias = tuple[str, Callable[[EmployeeDTO], str | float]]


class EmployeeTable(QTableWidget):
    def __init__(self, employees: list[EmployeeDTO]) -> None:
        super().__init__()

        self.columns: list[Column] = [
            ("Name", lambda employee: employee.personal.name),
            ("Surname", lambda employee: employee.personal.surname),
            ("Username", lambda employee: employee.credentials.username),
            ("Acronym", lambda employee: employee.credentials.acronym),
            ("FTE", lambda employee: employee.employment.fte),
            ("Utilization Rate", lambda employee: employee.employment.utilization_rate),
        ]

        self.setColumnCount(len(self.columns))
        self.setHorizontalHeaderLabels([label for (label, _) in self.columns])
        self.reset_table(employees)

    def reset_table(self, employees: list[EmployeeDTO]) -> None:
        self.setRowCount(len(employees))

        for row, employee in enumerate(employees):
            for col, (_, extractor) in enumerate(self.columns):
                value = extractor(employee)
                self.setItem(row, col, QTableWidgetItem(str(value)))
