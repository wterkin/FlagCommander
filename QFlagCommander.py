#!/usr/bin/python3.7
# -*- coding: utf-8 -*-

import sys

#try:
#    from PySide import QtCore
#    from PySide import QtWidgets as qt
#except:
#    from PyQt5 import QtCore
#from PyQt5 import QtWidgets as qt
#from PyQt5.QtCore import pyqtSlot as Slot
from PyQt5 import QtCore as core
from PyQt5 import QtWidgets as widgets

#from PyQt5 import QtGui as qtgui
import mainwindow as fc_mainwin
import sqlite3

#MAINFORM_UI = "mainform.ui"
TIMER_PERIOD = 1000 # ms
POLL_FOLDER_EACH = 10 # 60 # in periods

class QFCMainWindow(widgets.QMainWindow, fc_mainwin.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.mo_connection = sqlite3.connect("afc2.db")
        # *** Таймер
        self.mo_timer = core.QTimer()
        self.mo_timer.timeout.connect(self.__on_timer)
        self.mo_timer.start(TIMER_PERIOD)
        self.mo_timer_count = 0
        # *** Прогрессбар
        self.mo_progress = widgets.QProgressBar()
        self.mo_progress.format = "%v"
        self.mo_progress.setOrientation(core.Qt.Horizontal)
        self.mo_progress.setAlignment(core.Qt.AlignLeft)
        self.mo_progress.setRange(0, POLL_FOLDER_EACH)
        self.mo_progress.setValue(0)
        self.statusbar.addPermanentWidget(self.mo_progress,0)
        # *** Метка для вывода состояния
        self.mo_status = widgets.QLabel()
        self.mo_status.setAlignment(core.Qt.AlignLeft)
        self.mo_status.setText("Idle.")
        self.statusbar.addPermanentWidget(self.mo_status,0)

        # *** Сигналы
        self.act_add_flag.triggered.connect(
            self.__add_flag_action_triggered)
        self.act_edit_flag.triggered.connect(
            self.__edit_flag_action_triggered)
        self.act_delete_flag.triggered.connect(
            self.__delete_flag_action_triggered)

    def __add_flag_action_triggered(self):
        pass

    def __edit_flag_action_triggered(self):
        pass

    def __delete_flag_action_triggered(self):
        pass

    def __on_timer(self):
        """Обработчик таймера."""
        self.mo_timer_count +=1
        self.mo_progress.setValue(self.mo_timer_count)
        if self.mo_timer_count > POLL_FOLDER_EACH:

            self.mo_timer_count = 0
            self.mo_progress.reset()
            self.poll_folder()

    def poll_folder(self):
        """Процедура проверяет наличие флагов в папке"""
        self.mo_status.setText("Checking...")
        pass

def main():
    """Запускающая процедура."""
    lo_app = widgets.QApplication(sys.argv)
    lo_mainwin = QFCMainWindow()
    lo_mainwin.show()
    lo_app.exec()



if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()
