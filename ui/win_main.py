# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/main.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 800)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.speech_button = QtWidgets.QPushButton(self.centralwidget)
        self.speech_button.setGeometry(QtCore.QRect(20, 20, 512, 512))
        self.speech_button.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ui/res/mic.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.speech_button.setIcon(icon)
        self.speech_button.setIconSize(QtCore.QSize(512, 512))
        self.speech_button.setObjectName("speech_button")
        self.quote_text = QtWidgets.QLabel(self.centralwidget)
        self.quote_text.setGeometry(QtCore.QRect(20, 550, 891, 71))
        self.quote_text.setObjectName("quote_text")
        self.listView = QtWidgets.QListView(self.centralwidget)
        self.listView.setGeometry(QtCore.QRect(550, 20, 256, 511))
        self.listView.setObjectName("listView")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1200, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.quote_text.setText(_translate("MainWindow", "Sample text"))
