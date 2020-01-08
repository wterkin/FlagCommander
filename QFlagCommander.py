#!/usr/bin/python3.7
# -*- coding: utf-8 -*-

import sys
import os

#try:
#    from PySide import QtCore
# from PySide import QtWidgets as qt
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
FLAG_FOLDER = "/media/data/Projects/python/afc2/flags"
FLAG_EXT = ".flg"

class QFCMainWindow(widgets.QMainWindow, fc_mainwin.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # *** Переменные класса
        self.mo_connection = sqlite3.connect("afc2.db")
        self.mo_existing_flags = []
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
        self.statusbar.addPermanentWidget(self.mo_status,1)

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
        # *** Читаем папку с флагами
        lo_files = os.listdir(FLAG_FOLDER)
        lo_flags = filter(lambda x: x.endswith(FLAG_EXT), lo_files)
        for ls_flag in lo_flags:
            pass

    def query_flag(self, ps_flagname, ps_code):
        """Возвращает данные флага."""
        assert ps_flagname is not None, """Assert:
            [QFCMainWindow.query_flag]: No <ps_flagname> parameter
            specified!"""

        ls_sql = """select   F.ftype as aflagtype
                           , F.fcondition as aflagcondition
                           , F.fevent as aflagevent
                           , F.fname as aflagname
                           , F.fkill_after_use as aflagkillafteruse
                           , T.fname as atypename
                           , T.fcode as atypecode
                           , C.fname as aconditionname
                           , C.fcode as aconditioncode
                           , E.fname as aeventname
                           , E.fvalue as aeventvalue
                      from tbl_flags F
                      inner join tbl_types T
                        on     (T.id = F.ftype)
                           and (T.fstatus>0)
                      inner join tbl_conditions C
                        on     (C.id = F.fcondition)
                           and (C.fstatus>0)
                      inner join tbl_events E
                        on     (E.id = F.fevent)
                           and (E.fstatus>0)
                      where     (F.fname = %(pflagname)s)
                            and (F.fcode = %(pcode)s)
                            and (F.fstatus>0)"""
        lo_params = dict()
        lo_params["pflagname"] = ps_flagname
        lo_params["pcode"] = ps_code
        lo_cursor = self.mo_connection.get_cursor()
        lo_cursor.execute(ls_sql, lo_params)
def main():
    """Запускающая процедура."""
    lo_app = widgets.QApplication(sys.argv)
    lo_mainwin = QFCMainWindow()
    lo_mainwin.show()
    lo_app.exec()



if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()
