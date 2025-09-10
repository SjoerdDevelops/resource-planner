import sys
from ui.views import MainWindow
from infrastructure import db
from application.services import EmployeeService
from infrastructure.repositories import DBEmployeeRepository
from domain.entities import PersonalInfo, EmploymentDetails, CompanyCredentials
from ui.controllers import EmployeeControllerFactory
from .app import App


def main():
    db.init_db()
    employee_repository = DBEmployeeRepository()
    employee_service = EmployeeService(employee_repository)

    _ = employee_service.add(
        PersonalInfo("Sjoerd", "Kuitert"),
        EmploymentDetails(1.0, 0.8),
        CompanyCredentials("kuiters", "SKT"),
    )
    _ = employee_service.add(
        PersonalInfo("Jasper", "Schol"),
        EmploymentDetails(1.0, 0.9),
        CompanyCredentials("scholj", "JSL"),
    )

    app = App(sys.argv)
    app.employee_controller_factory = EmployeeControllerFactory(employee_service)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
