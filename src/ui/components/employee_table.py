from typing import Tuple, Callable, Any, List
from PySide6.QtWidgets import QTableWidget, QTableWidgetItem
from ui.dto import EmployeeDTO
from ui.contexts import employee_context

# Column = (header label, extractor function)
Column = Tuple[str, Callable[[EmployeeDTO], Any]]


class EmployeeTable(QTableWidget):
    def __init__(self):
        super().__init__()

        employees = employee_context.list_all()
        employee_context.data_changed.connect(self.on_data_changed)

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
        self.update_table(employees)

    def on_data_changed(self):
        employees = employee_context.list_all()
        self.update_table(employees)

    def update_table(self, employees: list[EmployeeDTO]):
        self.setRowCount(len(employees))

        for row, employee in enumerate(employees):
            for col, (_, extractor) in enumerate(self.columns):
                value: Any = extractor(employee)
                self.setItem(row, col, QTableWidgetItem(str(value)))
