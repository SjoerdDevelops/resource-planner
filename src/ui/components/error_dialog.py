from PySide6.QtWidgets import QDialog, QPushButton, QVBoxLayout, QLabel, QWidget


class ErrorDialog(QDialog):
    def __init__(self, message: str, parent: QWidget | None = None) -> None:
        super().__init__(parent)

        self._button: QPushButton = QPushButton()

        layout = QVBoxLayout()
        label = QLabel(message)
        layout.addWidget(label)
        layout.addWidget(self._button)
        self.setLayout(layout)
