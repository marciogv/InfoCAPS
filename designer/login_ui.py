# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        Dialog.setStyleSheet("background-color: rgb(94, 94, 94);")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(50, 70, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setStyleSheet("QLabel {\n"
"color: rgb(255, 255, 255);\n"
"border: 0px;\n"
"}")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(50, 120, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("QLabel {\n"
"color: rgb(255, 255, 255);\n"
"border: 0px;\n"
"}")
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(50, 230, 121, 23))
        self.pushButton.setStyleSheet("QPushButton{\n"
"background-color: rgb(63, 63, 63);\n"
"     border-width: 2px;\n"
"     border-radius: 10px;\n"
"     border-color: rgb(0, 170, 255);\n"
"     font: bold 14px;\n"
"     padding-left: 20px;\n"
"     padding-right: 20px;\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color:rgb(49, 49, 49);\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(210, 230, 131, 23))
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"background-color: rgb(63, 63, 63);\n"
"     border-width: 2px;\n"
"     border-radius: 10px;\n"
"     border-color: rgb(0, 170, 255);\n"
"     font: bold 14px;\n"
"     padding-left: 20px;\n"
"     padding-right: 20px;\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color:rgb(49, 49, 49);\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.lineEditName = QtWidgets.QLineEdit(Dialog)
        self.lineEditName.setGeometry(QtCore.QRect(130, 70, 201, 20))
        self.lineEditName.setStyleSheet("QLineEdit {\n"
"background-color: rgb(63, 63, 63);\n"
"     border-width: 2px;\n"
"     border-radius: 10px;\n"
"     border-color: rgb(0, 170, 255);\n"
"     font: bold 14px;\n"
"     padding-left: 20px;\n"
"     padding-right: 20px;\n"
"    color: rgb(255, 255, 255)\n"
"}")
        self.lineEditName.setObjectName("lineEditName")
        self.lineEditName_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEditName_2.setGeometry(QtCore.QRect(120, 120, 201, 20))
        self.lineEditName_2.setStyleSheet("QLineEdit {\n"
"background-color: rgb(63, 63, 63);\n"
"     border-width: 2px;\n"
"     border-radius: 10px;\n"
"     border-color: rgb(0, 170, 255);\n"
"     font: bold 14px;\n"
"     padding-left: 20px;\n"
"     padding-right: 20px;\n"
"    color: rgb(255, 255, 255)\n"
"}")
        self.lineEditName_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEditName_2.setObjectName("lineEditName_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Login"))
        self.label.setText(_translate("Dialog", "Usu??rio:"))
        self.label_2.setText(_translate("Dialog", "Senha:"))
        self.pushButton.setText(_translate("Dialog", "OK"))
        self.pushButton_2.setText(_translate("Dialog", "CANCELAR"))
