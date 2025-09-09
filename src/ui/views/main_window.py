from PySide6.QtWidgets import QMainWindow, QTabWidget
from .dashboard_view import DashboardView
from .employees_view import EmployeesView


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Resource Planning Tool")

        tabs = QTabWidget()
        _ = tabs.addTab(DashboardView(), "Dashboard")
        _ = tabs.addTab(EmployeesView(), "Employees")

        self.setCentralWidget(tabs)
