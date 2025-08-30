import sys
from PySide6.QtWidgets import QApplication
from main_window import MainWindow
from data.persistance import Persistance, Employee, create_employee
from typing import List


def main():
    app = QApplication(sys.argv)
    window = MainWindow()

    storage = Persistance()
    storage.store_employee(create_employee("Sjoerd", 1.0, 0.8))
    storage.store_employee(create_employee("Ana", 1.0, 0.9))

    employees: List[Employee] = storage.fetch_employees()
    for employee in employees:
        print(
            f"Id: {employee.id}, Name: {employee.name}, FTE: {employee.fte}, Utilization Rate: {employee.utilization_rate}"
        )

    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
