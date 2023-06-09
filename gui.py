# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


import typing
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
import sys


import checker
import download
import Addishon

class Ui_MainWindow(QMainWindow):
    def __init__(self) -> None:
        super(Ui_MainWindow, self).__init__()

        self.setObjectName("MainWindow")
        self.resize(725, 448)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.Zagolovok = QtWidgets.QLabel(self.centralwidget)
        self.Zagolovok.setGeometry(QtCore.QRect(170, 10, 411, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Zagolovok.setFont(font)
        self.Zagolovok.setObjectName("Zagolovok")

        self.special4 = QtWidgets.QLabel(self.centralwidget)
        self.special4.setGeometry(QtCore.QRect(270, 430, 211, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.special4.setFont(font)
        self.special4.setObjectName("special4")

        self.selectButton = QtWidgets.QPushButton(self.centralwidget)
        self.selectButton.setGeometry(QtCore.QRect(50, 120, 191, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.selectButton.setFont(font)
        self.selectButton.clicked.connect(self.selectFolder)
        self.selectButton.setObjectName("selectButton")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(80, 290, 491, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.setCentralWidget(self.centralwidget)

        self.updateButton = QtWidgets.QPushButton(self.centralwidget)
        self.updateButton.setGeometry(QtCore.QRect(450, 290, 191, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.updateButton.setFont(font)
        self.updateButton.clicked.connect(self.update)
        self.updateButton.setObjectName("updateButton")
        self.updateButton.setText('Обновить')


        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(30, 380, 661, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.progressBar.setFont(font)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.setCentralWidget(self.centralwidget)

#        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "AiracUpdate"))
        self.Zagolovok.setText(_translate("MainWindow", "Авматическое обновление Airac"))
        self.special4.setText(_translate("MainWindow", "By the10882 Special for УТЦ Ватрус"))
        self.selectButton.setText(_translate("MainWindow", "Выбор папки"))
        self.label.setText(_translate("MainWindow", "Укажите папку X-Plane"))

    def selectFolder(self):
        folder = str(QtWidgets.QFileDialog.getExistingDirectory(self, "выбор папки"))
        if folder == '':
            self.label.setText('Путь не указан')
            return
        actual = checker.check(folder)
        self.actual = actual
        if actual:
            self.label.setText('Ваша версия Airac актуальна')
        elif actual == None:
            self.label.setText('Путь указан неверно')
        else:
            self.label.setText('Ваша версия Airac устарела')

    def update(self):
        if not self.actual:
            actualHref = download.pars()
            self.progressBar.setProperty("value", 5)       
            download.download(actualHref[0])   
            self.progressBar.setProperty("value", 15)
            download.download(actualHref[1])   
            self.progressBar.setProperty("value", 25)
            download.download(actualHref[2])   
            self.progressBar.setProperty("value", 35)      

            download.unzip(actualHref[0])
            self.progressBar.setProperty("value", 55)
            download.unzip(actualHref[1])
            self.progressBar.setProperty("value", 75)
            download.unzip(actualHref[2])
            self.progressBar.setProperty("value", 95) 

            Addishon.addNDB()

            download.remove(actualHref[0])
            download.remove(actualHref[1])
            download.remove(actualHref[2])
            self.progressBar.setProperty("value", 100)      
            self.label.setText('Ваша версия Airac актуальна')
        else:
            return
        
    def notification(self):
        pass
def start():
    app = QApplication(sys.argv)
    window = Ui_MainWindow()

    window.show()
    sys.exit(app.exec_())