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
from typing import List
from domain.entities import (
    Employee,
    PersonalInfo,
    EmploymentDetails,
    CompanyCredentials,
)
from enum import IntEnum


class EmployeeColumns(IntEnum):
    NAME = 0
    SURNAME = 1
    USERNAME = 2
    ACRONYM = 3
    FTE = 4
    UTILIZATION_RATE = 5


class EmployeeTable(QTableWidget):
    def __init__(self):
        super().__init__()
        self.data_store = DBEmployeeRepository()
        self.data_store.add(
            Employee(
                PersonalInfo("Sjoerd", "Kuitert"),
                EmploymentDetails(1.0, 0.8),
                CompanyCredentials("kuiters", "SKT"),
            )
        )
        self.data_store.add(
            Employee(
                PersonalInfo("Jasper", "Schol"),
                EmploymentDetails(1.0, 0.9),
                CompanyCredentials("scholj", "JSL"),
            )
        )

        headers: List[str] = [
            "Name",
            "Surname",
            "Username",
            "Acronym",
            "FTE",
            "Utilization Rate",
        ]
        self.setColumnCount(len(headers))
        self.update_table()

    def update_table(self):
        employees: List[Employee] = self.data_store.list_all()
        self.setRowCount(len(employees))

        # TODO: Fix magic numbers
        for row, employee in enumerate(employees):
            self.setItem(row, 0, QTableWidgetItem(str(employee.personal.name)))
            self.setItem(row, 1, QTableWidgetItem(str(employee.personal.surname)))
            self.setItem(row, 2, QTableWidgetItem(str(employee.credentials.username)))
            self.setItem(row, 3, QTableWidgetItem(str(employee.credentials.acronym)))
            self.setItem(row, 4, QTableWidgetItem(str(employee.employment.fte)))
            self.setItem(
                row, 5, QTableWidgetItem(str(employee.employment.utilization_rate))
            )


class EmployeesView(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Employees view"))

        employee_table = EmployeeTable()
        layout.addWidget(employee_table)
        self.setLayout(layout)
