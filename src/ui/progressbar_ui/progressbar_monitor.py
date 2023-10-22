from PySide2.QtCore import *  # type: ignore
from PySide2.QtGui import *  # type: ignore
from PySide2.QtWidgets import *  # type: ignore


def get_progressbar_to_monitor(ui_form, name_componente, react_geometric: QRect, value: float) -> QProgressBar:
    progressBar = QProgressBar(ui_form)
    progressBar.setObjectName(name_componente)
    progressBar.setGeometry(react_geometric)
    progressBar.setValue(value)
    return progressBar