from PySide6.QtWidgets import QWidget, QVBoxLayout


class DashboardView(QWidget):
    def __init__(self) -> None:
        super().__init__()
        layout = QVBoxLayout()

        self.setLayout(layout)
