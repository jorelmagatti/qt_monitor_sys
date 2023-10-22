from PySide2.QtCore import *  # type: ignore
from PySide2.QtGui import *  # type: ignore
from PySide2.QtWidgets import *  # type: ignore

def get_icon_to_monitor(ui_form, name_componente) -> QIcon:
    icon = QIcon()
    iconThemeName = name_componente
    if QIcon.hasThemeIcon(iconThemeName):
        icon = QIcon.fromTheme(iconThemeName)
    else:
        icon.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)  
    return icon