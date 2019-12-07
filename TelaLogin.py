# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TelaLogin.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDesktopWidget


class Ui_TelaLogin(object):
    def setupUi(self, TelaLogin):
        TelaLogin.setObjectName("TelaLogin")
        TelaLogin.resize(549, 329)
        TelaLogin.setFixedSize(549,329)
        # Deixando a tela no centro
        c = TelaLogin.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        c.moveCenter(cp)
        TelaLogin.move(c.topLeft())
        #
        TelaLogin.setStyleSheet("font: 75 13pt \"Arial\";\n"
"color: rgb(238, 238, 236);\n"
"background-color: \'dodgerblue\';")
        self.centralwidget = QtWidgets.QWidget(TelaLogin)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(340, 60, 144, 186))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.formLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(2)
        self.gridLayout.setObjectName("gridLayout")
        self.txtUsername = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.txtUsername.setStyleSheet("background-color: rgb(238, 238, 236);\n"
"color: rgb(0, 0, 0);")
        self.txtUsername.setObjectName("txtUsername")
        self.gridLayout.addWidget(self.txtUsername, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.txtPassword = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.txtPassword.setStyleSheet("background-color: rgb(238, 238, 236);\n"
"color: rgb(0, 0, 0);")
        self.txtPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.txtPassword.setObjectName("txtPassword")
        self.gridLayout.addWidget(self.txtPassword, 3, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.gridLayout.addItem(spacerItem, 4, 0, 1, 1)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(200, 0, 101, 351))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(250, 0, 301, 51))
        self.label_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_3.setStyleSheet("background-color: rgb(85, 87, 83);\n"
"font: 81 22pt \"Arial\";")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.btnEntrar = QtWidgets.QPushButton(self.centralwidget)
        self.btnEntrar.setGeometry(QtCore.QRect(360, 250, 111, 41))
        self.btnEntrar.setStyleSheet("background-color: rgb(46, 52, 54);\n"
"selection-background-color: rgb(136, 138, 133);\n"
"color: rgb(238, 238, 236);")
        self.btnEntrar.setObjectName("btnEntrar")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(-10, 0, 261, 331))
        self.label_4.setStyleSheet("image: url(:/Icone/logo-icone.png);\n"
"background-color: rgb(85, 87, 83);")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        TelaLogin.setCentralWidget(self.centralwidget)

        self.retranslateUi(TelaLogin)
        QtCore.QMetaObject.connectSlotsByName(TelaLogin)

    def retranslateUi(self, TelaLogin):
        _translate = QtCore.QCoreApplication.translate
        TelaLogin.setWindowTitle(_translate("TelaLogin", "Login"))
        self.label.setText(_translate("TelaLogin", "Username"))
        self.label_2.setText(_translate("TelaLogin", "Password"))
        self.label_3.setText(_translate("TelaLogin", "Login"))
        self.btnEntrar.setText(_translate("TelaLogin", "Entrar"))
import resource_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TelaLogin = QtWidgets.QMainWindow()
    ui = Ui_TelaLogin()
    ui.setupUi(TelaLogin)
    TelaLogin.show()
    sys.exit(app.exec_())
