from PySide6.QtCore import QObject, Signal


class _ProjectContext(QObject):
    project_added: Signal = Signal(str)
    project_removed: Signal = Signal(str)
    project_updated: Signal = Signal(str)

    def __init__(self) -> None:
        super().__init__()


project_context: _ProjectContext = _ProjectContext()
