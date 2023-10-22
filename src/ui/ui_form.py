import sys
from PySide2.QtCore import *  # type: ignore
from PySide2.QtGui import *  # type: ignore
from PySide2.QtWidgets import *  # type: ignore
from src.ui.timer_ui.timer_monitor_ui import get_time_to_monitor
from src.ui.progressbar_ui.progressbar_monitor import get_progressbar_to_monitor
from src.ui.label_ui.label_monitor import get_label_to_monitor
from src.ui.icon_ui.icon_monitor import get_icon_to_monitor
from src.ui.font_ui.font_monitor import get_font_to_monitor

class Ui_ui_form(object):
    def setupUi(self, ui_form):
        self.validate_form_name(ui_form)
        self.set_icon_form(ui_form)
        self.set_progressbar_form(ui_form)
        self.set_timer_form()
        self.set_labels_form(ui_form)
        self.set_font()
        self.retranslateUi(ui_form)
        QMetaObject.connectSlotsByName(ui_form)
    
    def set_font(self):
        font = get_font_to_monitor(u"Ubuntu")
        self.title_label.setFont(font)
        self.title_label.setAlignment(Qt.AlignCenter)
    
    def set_icon_form(self, ui_form):
        icon = get_icon_to_monitor(ui_form, u"utilities-system-monitor")
        ui_form.setWindowIcon(icon)
    
    def set_progressbar_form(self, ui_form):
        self.progressBarCPU = get_progressbar_to_monitor(ui_form, u"progressBar", QRect(170, 70, 561, 23), 0)
        self.progressBarRAM = get_progressbar_to_monitor(ui_form, u"progressBar_2", QRect(170, 110, 561, 23), 0)
        self.progressBarSWAP = get_progressbar_to_monitor(ui_form, u"progressBar_3", QRect(170, 150, 561, 23), 0)
        self.progressBarDISK = get_progressbar_to_monitor(ui_form, u"progressBar_4", QRect(170, 190, 561, 23), 0)
    
    def set_timer_form(self):
        self.timer = get_time_to_monitor(self.progressBarCPU, self.progressBarRAM, self.progressBarSWAP, self.progressBarDISK)
        self.timer.start(1000)
    
    def set_labels_form(self, ui_form):
        self.cpu_label = get_label_to_monitor(ui_form,u"cpu_label", QRect(20, 77, 141, 21))
        self.mem_ram_label = get_label_to_monitor(ui_form, u"mem_ram_label", QRect(20, 110, 141, 21))
        self.mem_swap_label = get_label_to_monitor(ui_form, u"mem_swap_label", QRect(20, 150, 141, 21))
        self.disk_label = get_label_to_monitor(ui_form,u"disk_label",QRect(20, 190, 141, 21))
        self.title_label = get_label_to_monitor(ui_form, u"title_label", QRect(13, 20, 771, 31))

    def validate_form_name(self, ui_form):
        if not ui_form.objectName():
            ui_form.setObjectName(u"ui_form")
        ui_form.resize(800, 261)

    def retranslateUi(self, ui_form):
        ui_form.setWindowTitle(QCoreApplication.translate("ui_form", u"Monitor de Sistema Qt Python", None))
        self.cpu_label.setText(QCoreApplication.translate("ui_form", u"CPU %", None))
        self.mem_ram_label.setText(QCoreApplication.translate("ui_form", u"MEMORIA RAM %", None))
        self.mem_swap_label.setText(QCoreApplication.translate("ui_form", u"MEMORIA SWAP %", None))
        self.disk_label.setText(QCoreApplication.translate("ui_form", u"DISK %", None))
        self.title_label.setText(QCoreApplication.translate("ui_form", u"MONITOR DE SISTEMA QT PYTHON", None))
