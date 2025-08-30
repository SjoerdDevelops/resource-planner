from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel


class EmployeesView(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Employees view"))
        self.setLayout(layout)
