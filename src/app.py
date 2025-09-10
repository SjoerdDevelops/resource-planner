from PySide6.QtWidgets import QApplication
from ui.controllers import EmployeeControllerFactory


class App(QApplication):
    def __init__(self, argv: list[str]) -> None:
        super().__init__(argv)
        self.employee_controller_factory: EmployeeControllerFactory | None = None
