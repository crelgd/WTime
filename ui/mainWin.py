# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_WTime(object):
    def setupUi(self, WTime):
        WTime.setObjectName("WTime")
        WTime.resize(700, 400)
        self.centralwidget = QtWidgets.QWidget(WTime)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(230, 250, 250, 90))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(230, 130, 241, 20))
        self.lineEdit.setObjectName("lineEdit")
        WTime.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(WTime)
        self.statusbar.setObjectName("statusbar")
        WTime.setStatusBar(self.statusbar)

        self.retranslateUi(WTime)
        QtCore.QMetaObject.connectSlotsByName(WTime)

    def retranslateUi(self, WTime):
        _translate = QtCore.QCoreApplication.translate
        WTime.setWindowTitle(_translate("WTime", "WTime"))
        self.pushButton.setText(_translate("WTime", "Start"))