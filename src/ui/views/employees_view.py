from PySide6.QtWidgets import (
    QDialog,
    QMessageBox,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
)
from ui.components import EmployeeTable, NewEmployeeForm


class EmployeesView(QWidget):
    def __init__(self):
        super().__init__()

        # Table layout
        self.table_layout = QVBoxLayout()

        self.employee_table = EmployeeTable()
        self.table_layout.addWidget(self.employee_table)

        # Button layout
        self.button_layout = QVBoxLayout()

        self.add_button = QPushButton("Add")
        self.delete_button = QPushButton("Delete")
        self.save_button = QPushButton("Save")

        self.button_layout.addWidget(self.add_button)
        self.button_layout.addWidget(self.delete_button)
        self.button_layout.addWidget(self.save_button)
        self.button_layout.addStretch()  # pushes buttons to the top

        # Main layout
        main_layout = QHBoxLayout(self)
        main_layout.addLayout(self.table_layout)
        main_layout.addLayout(self.button_layout)
        self.setLayout(main_layout)

        # Callbacks
        self.add_button.clicked.connect(self.on_add_clicked)
        self.delete_button.clicked.connect(self.on_delete_clicked)
        self.save_button.clicked.connect(self.on_save_clicked)

    def on_add_clicked(self):
        dialog = NewEmployeeForm()

        if dialog.exec() == QDialog.DialogCode.Accepted:
            self.table_layout.update()

    def on_delete_clicked(self):
        row = self.employee_table.currentRow()

        if row >= 0:
            self.employee_table.removeRow(row)
        else:
            QMessageBox.critical(self, "Delete error", "No row selected to delete.")
            return

    def on_save_clicked(self):
        pass
