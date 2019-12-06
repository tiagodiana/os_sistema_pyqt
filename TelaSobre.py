# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TelaSobre.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDesktopWidget, QMessageBox


class Ui_TelaSobre(object):
    def setupUi(self, TelaSobre):
        TelaSobre.setObjectName("TelaSobre")
        TelaSobre.resize(622, 337)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Icone/logo-icone.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        TelaSobre.setWindowIcon(icon)
        # Deixando a janela de um tamanho fixo para não pode ser Maximizada
        TelaSobre.setFixedSize(622, 337)
        # Deixando a tela no centro
        c = TelaSobre.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        c.moveCenter(cp)
        TelaSobre.move(c.topLeft())
        #
        TelaSobre.setStyleSheet("background-color: \'dodgerblue\';\n"
"font: 75 14pt \"Arial\";\n"
"color:rgb(238, 238, 236);\n"
"")
        self.centralwidget = QtWidgets.QWidget(TelaSobre)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 10, 621, 91))
        self.label.setStyleSheet("image: url(:/Icone/logo-icone.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 100, 631, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 140, 141, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(60, 170, 195, 21))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(200, 250, 221, 31))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(50, 210, 541, 41))
        self.label_5.setObjectName("label_5")
        self.btnSair = QtWidgets.QPushButton(self.centralwidget)
        self.btnSair.setGeometry(QtCore.QRect(480, 290, 121, 31))
        self.btnSair.setStyleSheet("background-color: rgb(204, 0, 0);\n"
"")
        self.btnSair.setObjectName("btnSair")
        TelaSobre.setCentralWidget(self.centralwidget)

        self.retranslateUi(TelaSobre)
        QtCore.QMetaObject.connectSlotsByName(TelaSobre)


    def retranslateUi(self, TelaSobre):
        _translate = QtCore.QCoreApplication.translate
        TelaSobre.setWindowTitle(_translate("TelaSobre", "Sobre"))
        self.label_2.setText(_translate("TelaSobre", "Desenvolvedor:"))
        self.label_3.setText(_translate("TelaSobre", "Tiago Roberto Diana"))
        self.label_4.setText(_translate("TelaSobre", "Desenvolvido com PyQt"))
        self.label_5.setText(_translate("TelaSobre", "Software desenvolvido para gestão de ordem de serviço"))
        self.btnSair.setText(_translate("TelaSobre", "Sair"))
import resource_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TelaSobre = QtWidgets.QMainWindow()
    ui = Ui_TelaSobre()
    ui.setupUi(TelaSobre)
    TelaSobre.show()
    sys.exit(app.exec_())
