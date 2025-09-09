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
from typing import Final


class NewEmployeeForm(QDialog):
    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle("Add Employee Form")

        layout = QFormLayout()

        self._name_input: Final[QLineEdit] = QLineEdit()
        self._surname_input: Final[QLineEdit] = QLineEdit()
        self._fte_input: Final[QDoubleSpinBox] = QDoubleSpinBox()
        self._utilization_rate_input: Final[QDoubleSpinBox] = QDoubleSpinBox()
        self._username_input: Final[QLineEdit] = QLineEdit()
        self._acronym_input: Final[QLineEdit] = QLineEdit()

        self._submit_button: Final[QPushButton] = QPushButton("Submit")

        self._fte_input.setValue(1)
        self._fte_input.setMaximum(1)
        self._fte_input.setMinimum(0)
        self._fte_input.setDecimals(2)
        self._fte_input.setSingleStep(0.05)

        self._utilization_rate_input.setValue(0.8)
        self._utilization_rate_input.setMaximum(1)
        self._utilization_rate_input.setMinimum(0)
        self._utilization_rate_input.setDecimals(2)
        self._utilization_rate_input.setSingleStep(0.05)

        self._acronym_input.setMaxLength(3)

        layout.addRow("Name:", self._name_input)
        layout.addRow("Surname:", self._surname_input)
        layout.addRow("FTE:", self._fte_input)
        layout.addRow("Utilization Rate:", self._utilization_rate_input)
        layout.addRow("Username:", self._username_input)
        layout.addRow("Acronym:", self._acronym_input)

        self._buttons: Final[QDialogButtonBox] = QDialogButtonBox(
            QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel
        )
        _ = self._buttons.accepted.connect(self.on_accept)
        _ = self._buttons.rejected.connect(self.on_reject)

        layout.addRow(self._buttons)

        self.setLayout(layout)

    def on_accept(self) -> None:
        print("accepted")
        self.add_employee()
        self.accept()

    def on_reject(self) -> None:
        print("rejected")

    def get_data(
        self,
    ) -> tuple[PersonalInfoDTO, EmploymentDetailsDTO, CompanyCredentialsDTO]:
        personal_info = PersonalInfoDTO(
            name=self._name_input.text(), surname=self._surname_input.text()
        )
        employment_details = EmploymentDetailsDTO(
            fte=self._fte_input.value(),
            utilization_rate=self._utilization_rate_input.value(),
        )
        company_credentials = CompanyCredentialsDTO(
            username=self._username_input.text(), acronym=self._acronym_input.text()
        )
        return personal_info, employment_details, company_credentials

    def add_employee(self) -> None:
        employee_context.add_employee_requested.emit(
            PersonalInfoDTO(
                name=self._name_input.text(), surname=self._surname_input.text()
            ),
            EmploymentDetailsDTO(
                fte=self._fte_input.value(),
                utilization_rate=self._utilization_rate_input.value(),
            ),
            CompanyCredentialsDTO(
                username=self._username_input.text(), acronym=self._acronym_input.text()
            ),
        )
