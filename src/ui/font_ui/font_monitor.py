from PySide2.QtCore import *  # type: ignore
from PySide2.QtGui import *  # type: ignore
from PySide2.QtWidgets import *  # type: ignore

def get_font_to_monitor(name_componente) -> QFont:
    font = QFont()
    font.setFamily(name_componente)
    font.setPointSize(28)
    font.setBold(False)
    font.setWeight(50)
    return font