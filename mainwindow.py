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
        self.actAddFlag = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../../../usr/share/icons/gnome/22x22/actions/add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actAddFlag.setIcon(icon)
        self.actAddFlag.setObjectName("actAddFlag")
        self.actEdit = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../../../../../usr/share/icons/gnome/22x22/apps/accessories-text-editor.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actEdit.setIcon(icon1)
        self.actEdit.setObjectName("actEdit")
        self.actDelete = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../../../../../usr/share/icons/gnome/22x22/actions/remove.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actDelete.setIcon(icon2)
        self.actDelete.setObjectName("actDelete")
        self.actExit = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../../../../../usr/share/icons/gnome/22x22/actions/gtk-quit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actExit.setIcon(icon3)
        self.actExit.setObjectName("actExit")
        self.toolBar.addAction(self.actAddFlag)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actEdit)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actDelete)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actExit)
        self.toolBar.addSeparator()

        self.retranslateUi(MainWindow)
        self.toolBar.actionTriggered['QAction*'].connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actAddFlag.setText(_translate("MainWindow", "Добавить"))
        self.actAddFlag.setToolTip(_translate("MainWindow", "Добавить новый флаг"))
        self.actEdit.setText(_translate("MainWindow", "Редактировать"))
        self.actEdit.setToolTip(_translate("MainWindow", "Редактировать флаг"))
        self.actDelete.setText(_translate("MainWindow", "Удалить"))
        self.actDelete.setToolTip(_translate("MainWindow", "Удалить флаг"))
        self.actExit.setText(_translate("MainWindow", "Выйти"))
        self.actExit.setToolTip(_translate("MainWindow", "Выйти из программы"))
