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

import mainwindow as fc_mainwin

#MAINFORM_UI = "mainform.ui"

class QFCMainWindow(qt.QMainWindow, fc_mainwin.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
#        qt.QMainWindow.__init__(self)
        pass


def main():
    """Запускающая процедура."""
    #lo_app = QFlagCommander(sys.argv)
    lo_app = qt.QApplication(sys.argv)
    lo_mainwin = QFCMainWindow()
    lo_mainwin.show()
    lo_app.exec()
    #    lo_main_form_file = QFile(MAINFORM_UI)
#    lo_main_form_file.open(QFile.ReadOnly)

#    lo_loader = QUiLoader()
#    lo_window = lo_loader.load(lo_main_form_file)
#    lo_window.show()


if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()
