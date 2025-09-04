from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QTableWidget,
    QTableWidgetItem,
)
from infrastructure.repositories import (
    DBEmployeeRepository,
)
from typing import List, Any, Callable, Tuple
from domain.entities import (
    Employee,
    PersonalInfo,
    EmploymentDetails,
    CompanyCredentials,
)

# Column = (header label, extractor function)
Column = Tuple[str, Callable[[Employee], Any]]


class EmployeeTable(QTableWidget):
    def __init__(self):
        super().__init__()
        self.repository = DBEmployeeRepository()

        self.repository.add(
            Employee(
                PersonalInfo("Sjoerd", "Kuitert"),
                EmploymentDetails(1.0, 0.8),
                CompanyCredentials("kuiters", "SKT"),
            )
        )
        self.repository.add(
            Employee(
                PersonalInfo("Jasper", "Schol"),
                EmploymentDetails(1.0, 0.9),
                CompanyCredentials("scholj", "JSL"),
            )
        )

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
        self.update_table()

    def update_table(self):
        employees: List[Employee] = self.repository.list_all()
        self.setRowCount(len(employees))

        for row, employee in enumerate(employees):
            for col, (_, extractor) in enumerate(self.columns):
                value: Any = extractor(employee)
                self.setItem(row, col, QTableWidgetItem(str(value)))


class EmployeesView(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Employees view"))

        employee_table = EmployeeTable()
        layout.addWidget(employee_table)
        self.setLayout(layout)
