# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(456, 786)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("\n"
"background-color: #24224D")
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(-1, -1, 480, 270))
        self.frame.setStyleSheet("background-color: #CA417A")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(50, 0, 381, 91))
        font = QtGui.QFont()
        font.setFamily("Coolvetica Condensed Rg")
        font.setPointSize(48)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("color:#C0C0F1")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(150, 100, 151, 151))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("../../../Downloads/exchange (1).png"))
        self.label_2.setScaledContents(True)
        self.label_2.setWordWrap(False)
        self.label_2.setOpenExternalLinks(False)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(140, 100, 171, 151))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("exchange (1).png"))
        self.label_3.setScaledContents(True)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.input_currency = QtWidgets.QLineEdit(self.centralwidget)
        self.input_currency.setGeometry(QtCore.QRect(50, 320, 380, 60))
        font = QtGui.QFont()
        font.setFamily("Ebrima")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.input_currency.setFont(font)
        self.input_currency.setStyleSheet("background-color:#24224D;\n"
"border: 2px solid #CA417A;\n"
"border-radius:30;\n"
"color:#C0C0F1")
        self.input_currency.setText("")
        self.input_currency.setAlignment(QtCore.Qt.AlignCenter)
        self.input_currency.setObjectName("input_currency")
        self.input_amount = QtWidgets.QLineEdit(self.centralwidget)
        self.input_amount.setGeometry(QtCore.QRect(50, 420, 380, 60))
        font = QtGui.QFont()
        font.setFamily("Ebrima")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.input_amount.setFont(font)
        self.input_amount.setStyleSheet("background-color:#24224D;\n"
"border: 2px solid #CA417A;\n"
"border-radius:30;\n"
"color:#C0C0F1")
        self.input_amount.setText("")
        self.input_amount.setAlignment(QtCore.Qt.AlignCenter)
        self.input_amount.setObjectName("input_amount")
        self.output_currency = QtWidgets.QLineEdit(self.centralwidget)
        self.output_currency.setGeometry(QtCore.QRect(50, 520, 380, 60))
        font = QtGui.QFont()
        font.setFamily("Ebrima")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.output_currency.setFont(font)
        self.output_currency.setStyleSheet("background-color:#24224D;\n"
"border: 2px solid #CA417A;\n"
"border-radius:30;\n"
"color:#C0C0F1")
        self.output_currency.setText("")
        self.output_currency.setAlignment(QtCore.Qt.AlignCenter)
        self.output_currency.setObjectName("output_currency")
        self.output_amount = QtWidgets.QLineEdit(self.centralwidget)
        self.output_amount.setGeometry(QtCore.QRect(50, 620, 380, 60))
        font = QtGui.QFont()
        font.setFamily("Ebrima")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.output_amount.setFont(font)
        self.output_amount.setStyleSheet("background-color:#24224D;\n"
"border: 2px solid #CA417A;\n"
"border-radius:30;\n"
"color:#C0C0F1")
        self.output_amount.setText("")
        self.output_amount.setAlignment(QtCore.Qt.AlignCenter)
        self.output_amount.setObjectName("output_amount")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(50, 720, 380, 60))
        font = QtGui.QFont()
        font.setFamily("Coolvetica Condensed Rg")
        font.setPointSize(22)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton {\n"
"    color: white;\n"
"    background-color:#CA417A;\n"
"    border-radius:30;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color:#B52FA9;\n"
"}")
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Currency Converter"))
        self.pushButton.setText(_translate("MainWindow", "CONVERT"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())