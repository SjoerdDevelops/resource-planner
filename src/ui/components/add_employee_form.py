from PySide6.QtWidgets import (
    QDialogButtonBox,
    QFormLayout,
    QLineEdit,
    QDoubleSpinBox,
    QPushButton,
    QDialog,
    QWidget,
)
from ui.contexts import employee_context
from ui.dto import PersonalInfoDTO, EmploymentDetailsDTO, CompanyCredentialsDTO
from typing import Final
from .error_dialog import ErrorDialog
from pydantic import ValidationError


class AddEmployeeForm(QDialog):
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)

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

    def get_data(
        self,
    ) -> tuple[PersonalInfoDTO, EmploymentDetailsDTO, CompanyCredentialsDTO]:
        try:
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
        except ValidationError as e:
            messages = [error["msg"] for error in e.errors()]
            error_text = "\n".join(messages)
            raise ValueError(error_text)

    def on_accept(self) -> None:
        try:
            [personal, employment, credentials] = self.get_data()
            employee_context.add_employee_requested.emit(
                personal, employment, credentials
            )
            self.accept()

        except Exception as e:
            dialog = ErrorDialog(str(e), self)
            _ = dialog.exec()

    def on_reject(self) -> None:
        print("rejected")
