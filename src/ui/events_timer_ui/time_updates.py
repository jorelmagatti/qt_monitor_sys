from PySide2.QtCore import *  # type: ignore
from PySide2.QtGui import *  # type: ignore
from PySide2.QtWidgets import *  # type: ignore

def update_progress_component(q_progress_bar: QProgressBar, get_data_usage):
    return lambda : q_progress_bar.setValue(get_data_usage())


