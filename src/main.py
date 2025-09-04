import sys
from PySide6.QtWidgets import QApplication
from main_window import MainWindow
from infrastructure import db


def main():
    db.init_db()

    app = QApplication(sys.argv)
    window = MainWindow()

    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
