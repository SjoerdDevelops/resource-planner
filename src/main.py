import sys
from PySide6.QtWidgets import QApplication
from ui.views import MainWindow
from infrastructure import db
from application.services import EmployeeService
from infrastructure.repositories import DBEmployeeRepository
from domain.entities import PersonalInfo, EmploymentDetails, CompanyCredentials


def main():
    db.init_db()
    repository = DBEmployeeRepository()
    service = EmployeeService(repository)

    service.add_employee(
        PersonalInfo("Sjoerd", "Kuitert"),
        EmploymentDetails(1.0, 0.8),
        CompanyCredentials("kuiters", "SKT"),
    )
    service.add_employee(
        PersonalInfo("Jasper", "Schol"),
        EmploymentDetails(1.0, 0.9),
        CompanyCredentials("scholj", "JSL"),
    )

    app = QApplication(sys.argv)
    window = MainWindow()

    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
