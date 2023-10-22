from PySide2.QtCore import *  # type: ignore
from PySide2.QtGui import *  # type: ignore
from PySide2.QtWidgets import *  # type: ignore

def get_label_to_monitor(ui_form, name_componente, react_geometric: QRect) -> QLabel:
    label_monitor = QLabel(ui_form)
    label_monitor.setObjectName(name_componente)
    label_monitor.setGeometry(react_geometric)
    return label_monitor