# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/mawinsukmongkol/Desktop/CN212/benchmarkpage.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1100, 780)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(20, 0, 200, 60))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setStyleSheet("color:rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(25, 5, 200, 60))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: #aa00ff;")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(400, 50, 750, 750))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("/Users/mawinsukmongkol/Desktop/CN212/assets/circleloop3.gif"))
        self.label_3.setObjectName("label_3")
        self.exitButton = QtWidgets.QPushButton(self.frame)
        self.exitButton.setGeometry(QtCore.QRect(1020, 15, 93, 28))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.exitButton.setFont(font)
        self.exitButton.setStyleSheet("\n"
"QPushButton{color: rgba(255, 255, 255, 100);}\n"
"QPushButton:hover{\n"
"    \n"
"    color: rgb(39, 47, 226);\n"
"}")
        self.exitButton.setObjectName("exitButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(80, 650, 131, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton{background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0.414773, stop:0 #aa00ff, stop:1 #ff73d3);\\n\"\"padding: 10px;\n"
"padding: 10px;\n"
"text-align: center;\n"
"border-style: none;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0.414773, stop:0 #ff73d3, stop:1 #aa00ff );\n"
"    margin-left:5px;\n"
"    margin-top:5px;\n"
"    font-size: 14px;\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setGeometry(QtCore.QRect(250, 650, 131, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("QPushButton{background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0.414773, stop:0 #aa00ff, stop:1 #ff73d3);\\n\"\"padding: 10px;\n"
"padding: 10px;\n"
"text-align: center;\n"
"border-style: none;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0.414773, stop:0 #ff73d3, stop:1 #aa00ff );\n"
"    margin-left:5px;\n"
"    margin-top:5px;\n"
"    font-size: 14px;\n"
"}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_15 = QtWidgets.QLabel(self.frame)
        self.label_15.setGeometry(QtCore.QRect(80, 105, 350, 60))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("\n"
"color: #aa00ff;")
        self.label_15.setObjectName("label_15")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(70, 110, 641, 461))
        self.frame_2.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.frame_2)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(60, 110, 561, 361))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.lbl_delete_bench = QtWidgets.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lbl_delete_bench.setFont(font)
        self.lbl_delete_bench.setStyleSheet("color: rgb(255, 255, 255);")
        self.lbl_delete_bench.setObjectName("lbl_delete_bench")
        self.gridLayout_2.addWidget(self.lbl_delete_bench, 4, 0, 1, 1)
        self.lbl_create_bench = QtWidgets.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lbl_create_bench.setFont(font)
        self.lbl_create_bench.setStyleSheet("color: rgb(255, 255, 255);")
        self.lbl_create_bench.setObjectName("lbl_create_bench")
        self.gridLayout_2.addWidget(self.lbl_create_bench, 1, 0, 1, 1)
        self.lbl_write_bench = QtWidgets.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lbl_write_bench.setFont(font)
        self.lbl_write_bench.setStyleSheet("color: rgb(255, 255, 255);")
        self.lbl_write_bench.setObjectName("lbl_write_bench")
        self.gridLayout_2.addWidget(self.lbl_write_bench, 2, 0, 1, 1)
        self.write_bench = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.write_bench.setStyleSheet("color: rgb(218, 218, 218);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.write_bench.setObjectName("write_bench")
        self.gridLayout_2.addWidget(self.write_bench, 2, 1, 1, 1)
        self.lbl_read_bench = QtWidgets.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lbl_read_bench.setFont(font)
        self.lbl_read_bench.setStyleSheet("color: rgb(255, 255, 255);")
        self.lbl_read_bench.setObjectName("lbl_read_bench")
        self.gridLayout_2.addWidget(self.lbl_read_bench, 3, 0, 1, 1)
        self.lbl_memory_bench = QtWidgets.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lbl_memory_bench.setFont(font)
        self.lbl_memory_bench.setStyleSheet("color: rgb(255, 255, 255);")
        self.lbl_memory_bench.setObjectName("lbl_memory_bench")
        self.gridLayout_2.addWidget(self.lbl_memory_bench, 5, 0, 1, 1)
        self.read_bench = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.read_bench.setStyleSheet("color: rgb(218, 218, 218);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.read_bench.setObjectName("read_bench")
        self.gridLayout_2.addWidget(self.read_bench, 3, 1, 1, 1)
        self.memory_bench = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.memory_bench.setStyleSheet("color: rgb(218, 218, 218);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.memory_bench.setObjectName("memory_bench")
        self.gridLayout_2.addWidget(self.memory_bench, 5, 1, 1, 1)
        self.create_bench = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.create_bench.setStyleSheet("color: rgb(218, 218, 218);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.create_bench.setObjectName("create_bench")
        self.gridLayout_2.addWidget(self.create_bench, 1, 1, 1, 1)
        self.cpu_bench = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.cpu_bench.setStyleSheet("color: rgb(218, 218, 218);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.cpu_bench.setObjectName("cpu_bench")
        self.gridLayout_2.addWidget(self.cpu_bench, 0, 1, 1, 1)
        self.delete_bench = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.delete_bench.setStyleSheet("color: rgb(218, 218, 218);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.delete_bench.setObjectName("delete_bench")
        self.gridLayout_2.addWidget(self.delete_bench, 4, 1, 1, 1)
        self.lbl_cpu_bench = QtWidgets.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lbl_cpu_bench.setFont(font)
        self.lbl_cpu_bench.setStyleSheet("color: rgb(255, 255, 255);")
        self.lbl_cpu_bench.setObjectName("lbl_cpu_bench")
        self.gridLayout_2.addWidget(self.lbl_cpu_bench, 0, 0, 1, 1)
        self.gridLayout_2.setColumnStretch(0, 1)
        self.gridLayout_2.setColumnStretch(1, 2)
        self.label_3.raise_()
        self.label_2.raise_()
        self.label.raise_()
        self.exitButton.raise_()
        self.pushButton_2.raise_()
        self.label_15.raise_()
        self.frame_2.raise_()
        self.verticalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "SUPER BENMARK"))
        self.label_2.setText(_translate("MainWindow", "SUPER BENMARK"))
        self.exitButton.setText(_translate("MainWindow", "X"))
        self.pushButton_2.setText(_translate("MainWindow", "BACK"))
        self.pushButton_3.setText(_translate("MainWindow", "START"))
        self.label_15.setText(_translate("MainWindow", "Benchmark"))
        self.lbl_delete_bench.setText(_translate("MainWindow", "Delete Bench"))
        self.lbl_create_bench.setText(_translate("MainWindow", "Create Bench"))
        self.lbl_write_bench.setText(_translate("MainWindow", "write Bench"))
        self.write_bench.setText(_translate("MainWindow", "-"))
        self.lbl_read_bench.setText(_translate("MainWindow", "Read Bench"))
        self.lbl_memory_bench.setText(_translate("MainWindow", "Memory Bench"))
        self.read_bench.setText(_translate("MainWindow", "-"))
        self.memory_bench.setText(_translate("MainWindow", "-"))
        self.create_bench.setText(_translate("MainWindow", "-"))
        self.cpu_bench.setText(_translate("MainWindow", "-"))
        self.delete_bench.setText(_translate("MainWindow", "-"))
        self.lbl_cpu_bench.setText(_translate("MainWindow", "CPU Bench"))
