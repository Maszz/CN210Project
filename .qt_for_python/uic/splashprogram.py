# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/mawinsukmongkol/Desktop/CN212/splashprogram.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Splashscreen(object):
    def setupUi(self, Splashscreen):
        Splashscreen.setObjectName("Splashscreen")
        Splashscreen.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(Splashscreen)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.splashframe = QtWidgets.QFrame(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI Light")
        self.splashframe.setFont(font)
        self.splashframe.setStyleSheet("background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(0, 0, 0, 0));")
        self.splashframe.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.splashframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.splashframe.setObjectName("splashframe")
        self.label = QtWidgets.QLabel(self.splashframe)
        self.label.setGeometry(QtCore.QRect(-170, 40, 781, 111))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(255, 255, 255);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.progressBar = QtWidgets.QProgressBar(self.splashframe)
        self.progressBar.setGeometry(QtCore.QRect(110, 140, 551, 23))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.progressBar.setFont(font)
        self.progressBar.setStyleSheet("QProgressBar{\n"
"    \n"
"    \n"
"    \n"
"    background-color: qlineargradient(spread:pad, x1:1, y1:0.335, x2:0.338, y2:0.437682, stop:0 rgba(0, 0, 0, 50), stop:1 rgba(255, 255, 255, 207));\n"
"    border-radius: 10px;\n"
"    text-align: right;\n"
"    \n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QProgressBar::chunk {\n"
"    border-radius: 10px;\n"
"    \n"
"    \n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.369, x2:1, y2:0.364, stop:0 rgba(0, 179, 255, 200), stop:1 rgba(255, 255, 255, 20));\n"
"}")
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.label_2 = QtWidgets.QLabel(self.splashframe)
        self.label_2.setGeometry(QtCore.QRect(230, 180, 781, 20))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.logoImage = QtWidgets.QLabel(self.splashframe)
        self.logoImage.setGeometry(QtCore.QRect(80, 50, 621, 481))
        self.logoImage.setText("")
        self.logoImage.setPixmap(QtGui.QPixmap("/Users/mawinsukmongkol/Desktop/CN212/logoImage.png"))
        self.logoImage.setObjectName("logoImage")
        self.logoImage.raise_()
        self.label.raise_()
        self.progressBar.raise_()
        self.label_2.raise_()
        self.verticalLayout.addWidget(self.splashframe)
        Splashscreen.setCentralWidget(self.centralwidget)

        self.retranslateUi(Splashscreen)
        QtCore.QMetaObject.connectSlotsByName(Splashscreen)

    def retranslateUi(self, Splashscreen):
        _translate = QtCore.QCoreApplication.translate
        Splashscreen.setWindowTitle(_translate("Splashscreen", "MainWindow"))
        self.label.setText(_translate("Splashscreen", "BENCHMARK"))
        self.label_2.setText(_translate("Splashscreen", "loading..."))
import 2แก้_rc
import logo_rc