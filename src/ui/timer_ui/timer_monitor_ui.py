from PySide2.QtCore import *  # type: ignore
from PySide2.QtGui import *  # type: ignore
from PySide2.QtWidgets import *  # type: ignore
from src.util.ui_util import get_percentual_usage_cpu, get_percentual_usage_memory_ram,get_percentual_usage_memory_swap,get_percentual_usage_disk_root
from src.ui.events_timer_ui.time_updates import update_progress_component

def get_time_to_monitor(progressBarCPU: QProgressBar,
                        progressBarRAM: QProgressBar,
                        progressBarSWAP: QProgressBar,
                        progressBarDISK: QProgressBar) -> QTimer:
    timer = QTimer()
    timer.timeout.connect(update_progress_component(progressBarCPU, get_percentual_usage_cpu))
    timer.timeout.connect(update_progress_component(progressBarRAM, get_percentual_usage_memory_ram))
    timer.timeout.connect(update_progress_component(progressBarSWAP, get_percentual_usage_memory_swap))
    timer.timeout.connect(update_progress_component(progressBarDISK, get_percentual_usage_disk_root))
    return timer