from PySide6.QtWidgets import (
    QDialogButtonBox,
    QFormLayout,
    QLineEdit,
    QDoubleSpinBox,
    QPushButton,
    QDialog,
)
from ui.contexts import employee_context
from ui.dto import PersonalInfoDTO, EmploymentDetailsDTO, CompanyCredentialsDTO


class NewEmployeeForm(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Add Employee Form")

        layout = QFormLayout()

        self.name_input = QLineEdit()
        self.surname_input = QLineEdit()
        self.fte_input = QDoubleSpinBox()
        self.utilization_rate_input = QDoubleSpinBox()
        self.username_input = QLineEdit()
        self.acronym_input = QLineEdit()
        self.submit_button = QPushButton("Submit")

        self.fte_input.setValue(1)
        self.fte_input.setMaximum(1)
        self.fte_input.setMinimum(0)
        self.fte_input.setDecimals(2)
        self.fte_input.setSingleStep(0.05)

        self.utilization_rate_input.setValue(0.8)
        self.utilization_rate_input.setMaximum(1)
        self.utilization_rate_input.setMinimum(0)
        self.utilization_rate_input.setDecimals(2)
        self.utilization_rate_input.setSingleStep(0.05)

        self.acronym_input.setMaxLength(3)

        layout.addRow("Name:", self.name_input)
        layout.addRow("Surname:", self.surname_input)
        layout.addRow("FTE:", self.fte_input)
        layout.addRow("Utilization Rate:", self.utilization_rate_input)
        layout.addRow("Username:", self.username_input)
        layout.addRow("Acronym:", self.acronym_input)

        self.buttons = QDialogButtonBox(
            QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel
        )
        self.buttons.accepted.connect(self.on_accept)
        self.buttons.rejected.connect(self.on_reject)

        layout.addRow(self.buttons)

        self.setLayout(layout)

    def on_accept(self):
        print("accepted")
        self.add_employee()
        self.accept()

    def on_reject(self):
        print("rejected")

    def get_data(self):
        return {
            "name": self.name_input.text(),
            "surname": self.surname_input.text(),
            "fte": self.fte_input.text(),
            "utilization_rate": self.fte_input.text(),
            "username": self.username_input.text(),
            "acronym": self.acronym_input.text(),
        }

    def add_employee(self):
        employee_context.add_employee_requested.emit(
            PersonalInfoDTO(self.name_input.text(), self.surname_input.text()),
            EmploymentDetailsDTO(
                self.fte_input.value(), self.utilization_rate_input.value()
            ),
            CompanyCredentialsDTO(
                self.username_input.text(), self.acronym_input.text()
            ),
        )
