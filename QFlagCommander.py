#!/usr/bin/python3.7
# -*- coding: utf-8 -*-

import sys

try:
    from PySide import QtCore
    from PySide import QtWidgets as qt
except:
    from PyQt5.QtCore import pyqtSlot as Slot
    from PyQt5 import QtCore
    from PyQt5 import QtWidgets as qt

from PyQt5 import QtCore as qtcore 

import mainwindow as fc_mainwin
import sqlite3

#MAINFORM_UI = "mainform.ui"
TIMER_PERIOD = 1000 # ms

class QFCMainWindow(qt.QMainWindow, fc_mainwin.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.mo_connection = sqlite3.connect("afc2.db")
        self.mo_timer = qtcore.QTimer()
        self.mo_timer.timeout.connect(self.__on_timer)
        self.mo_timer.start(TIMER_PERIOD)
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

        pass

def main():
    """Запускающая процедура."""
    lo_app = qt.QApplication(sys.argv)
    lo_mainwin = QFCMainWindow()
    lo_mainwin.show()
    lo_app.exec()



if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()
