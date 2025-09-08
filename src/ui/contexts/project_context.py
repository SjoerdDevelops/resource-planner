from PySide6.QtCore import QObject, Signal
from typing import Any


class _ProjectContext(QObject):
    project_added = Signal(str)
    project_removed = Signal(str)
    project_updated = Signal(str)

    _projects: list[Any] = []

    def __init__(self):
        super().__init__()


project_context = _ProjectContext()
