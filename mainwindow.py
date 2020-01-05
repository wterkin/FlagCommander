# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(606, 308)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.horizontalLayout.addWidget(self.tableWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.act_add_flag = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../../../usr/share/icons/gnome/22x22/actions/add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.act_add_flag.setIcon(icon)
        self.act_add_flag.setObjectName("act_add_flag")
        self.act_edit_flag = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../../../../../usr/share/icons/gnome/22x22/apps/accessories-text-editor.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.act_edit_flag.setIcon(icon1)
        self.act_edit_flag.setObjectName("act_edit_flag")
        self.act_delete_flag = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../../../../../usr/share/icons/gnome/22x22/actions/remove.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.act_delete_flag.setIcon(icon2)
        self.act_delete_flag.setObjectName("act_delete_flag")
        self.act_exit = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../../../../../usr/share/icons/gnome/22x22/actions/gtk-quit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.act_exit.setIcon(icon3)
        self.act_exit.setObjectName("act_exit")
        self.toolBar.addAction(self.act_add_flag)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.act_edit_flag)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.act_delete_flag)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.act_exit)
        self.toolBar.addSeparator()

        self.retranslateUi(MainWindow)
        self.toolBar.actionTriggered['QAction*'].connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.act_add_flag.setText(_translate("MainWindow", "Добавить"))
        self.act_add_flag.setToolTip(_translate("MainWindow", "Добавить новый флаг"))
        self.act_edit_flag.setText(_translate("MainWindow", "Редактировать"))
        self.act_edit_flag.setToolTip(_translate("MainWindow", "Редактировать флаг"))
        self.act_delete_flag.setText(_translate("MainWindow", "Удалить"))
        self.act_delete_flag.setToolTip(_translate("MainWindow", "Удалить флаг"))
        self.act_exit.setText(_translate("MainWindow", "Выйти"))
        self.act_exit.setToolTip(_translate("MainWindow", "Выйти из программы"))
