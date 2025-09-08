from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel
from ui.components import NewEmployeeForm


class DashboardView(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()

        self.setLayout(layout)
