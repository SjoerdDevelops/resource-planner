from PySide6.QtWidgets import QMainWindow, QTabWidget
from .dashboard_view import DashboardView
from .employees_view import EmployeesView


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Resource Planning Tool")

        tabs = QTabWidget()
        tabs.addTab(DashboardView(), "Dashboard")
        tabs.addTab(EmployeesView(), "Employees")

        self.setCentralWidget(tabs)
