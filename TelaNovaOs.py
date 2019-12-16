# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TelaNovaOs.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!



from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDesktopWidget


class Ui_TelaNovaOs(object):
    def setupUi(self, TelaNovaOs):
        TelaNovaOs.setObjectName("TelaNovaOs")
        TelaNovaOs.resize(718, 546)
        # Deixando a janela de um tamanho fixo para não pode ser Maximizada
        TelaNovaOs.setFixedSize(718, 546)
        # Deixando a tela no centro
        c = TelaNovaOs.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        c.moveCenter(cp)
        TelaNovaOs.move(c.topLeft())
        #
        font = QtGui.QFont()
        font.setFamily("Hack")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        TelaNovaOs.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Icone/logo-icone.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        TelaNovaOs.setWindowIcon(icon)
        TelaNovaOs.setStyleSheet("background-color: \'dodgerblue\';\n"
"font: 75 13pt \"Hack\";\n"
"color: rgb(238, 238, 236);")
        self.centralwidget = QtWidgets.QWidget(TelaNovaOs)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 721, 71))
        font = QtGui.QFont()
        font.setFamily("FreeSans")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label.setFont(font)
        self.label.setStyleSheet("font: 75 18pt \"FreeSans\";\n"
"background-color: rgb(85, 87, 83);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(60, 110, 81, 21))
        self.label_2.setObjectName("label_2")
        self.txtMarca = QtWidgets.QLineEdit(self.centralwidget)
        self.txtMarca.setGeometry(QtCore.QRect(200, 210, 141, 25))
        self.txtMarca.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(238, 238, 236);")
        self.txtMarca.setObjectName("txtMarca")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(60, 180, 81, 21))
        self.label_3.setObjectName("label_3")
        self.cmbCliente = QtWidgets.QComboBox(self.centralwidget)
        self.cmbCliente.setGeometry(QtCore.QRect(60, 140, 391, 25))
        self.cmbCliente.setStyleSheet("color: rgb(0, 0, 0);\n"
"selection-background-color: rgb(136, 138, 133);\n"
"background-color: rgb(238, 238, 236);")
        self.cmbCliente.setObjectName("cmbCliente")
        self.cmbTipo = QtWidgets.QComboBox(self.centralwidget)
        self.cmbTipo.setGeometry(QtCore.QRect(60, 210, 131, 25))
        self.cmbTipo.setStyleSheet("color: rgb(0, 0, 0);\n"
"selection-background-color: rgb(136, 138, 133);\n"
"background-color: rgb(238, 238, 236);")
        self.cmbTipo.setObjectName("cmbTipo")
        self.cmbTipo.addItem("")
        self.cmbTipo.addItem("")
        self.cmbTipo.addItem("")
        self.cmbTipo.addItem("")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(200, 180, 81, 21))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(360, 180, 81, 21))
        self.label_5.setObjectName("label_5")
        self.txtModelo = QtWidgets.QLineEdit(self.centralwidget)
        self.txtModelo.setGeometry(QtCore.QRect(360, 210, 141, 25))
        self.txtModelo.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(238, 238, 236);")
        self.txtModelo.setObjectName("txtModelo")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(520, 180, 81, 21))
        self.label_6.setObjectName("label_6")
        self.txtNumSerie = QtWidgets.QLineEdit(self.centralwidget)
        self.txtNumSerie.setGeometry(QtCore.QRect(520, 210, 121, 25))
        self.txtNumSerie.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(238, 238, 236);")
        self.txtNumSerie.setObjectName("txtNumSerie")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(60, 250, 81, 21))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(360, 250, 81, 21))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(260, 430, 61, 24))
        self.label_9.setStyleSheet("font: 75 15pt \"Hack\";")
        self.label_9.setObjectName("label_9")
        self.txtValor = QtWidgets.QLineEdit(self.centralwidget)
        self.txtValor.setGeometry(QtCore.QRect(360, 430, 101, 25))
        self.txtValor.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(238, 238, 236);")
        self.txtValor.setObjectName("txtValor")
        self.btnCadastrar = QtWidgets.QPushButton(self.centralwidget)
        self.btnCadastrar.setGeometry(QtCore.QRect(290, 480, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Hack")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.btnCadastrar.setFont(font)
        self.btnCadastrar.setStyleSheet("background-color: rgb(78, 154, 6);\n"
"font: 75 14pt \"Hack\";\n"
"color: rgb(238, 238, 236);")
        self.btnCadastrar.setObjectName("btnCadastrar")
        self.txtDefeito = QtWidgets.QTextEdit(self.centralwidget)
        self.txtDefeito.setGeometry(QtCore.QRect(60, 280, 281, 121))
        self.txtDefeito.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(238, 238, 236);")
        self.txtDefeito.setTabChangesFocus(True)
        self.txtDefeito.setObjectName("txtDefeito")
        self.txtSolucao = QtWidgets.QTextEdit(self.centralwidget)
        self.txtSolucao.setGeometry(QtCore.QRect(360, 280, 281, 121))
        self.txtSolucao.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(238, 238, 236);")
        self.txtSolucao.setTabChangesFocus(True)
        self.txtSolucao.setObjectName("txtSolucao")
        TelaNovaOs.setCentralWidget(self.centralwidget)

        self.retranslateUi(TelaNovaOs)
        QtCore.QMetaObject.connectSlotsByName(TelaNovaOs)
        TelaNovaOs.setTabOrder(self.cmbCliente, self.cmbTipo)
        TelaNovaOs.setTabOrder(self.cmbTipo, self.txtMarca)
        TelaNovaOs.setTabOrder(self.txtMarca, self.txtModelo)
        TelaNovaOs.setTabOrder(self.txtModelo, self.txtNumSerie)
        TelaNovaOs.setTabOrder(self.txtNumSerie, self.txtDefeito)
        TelaNovaOs.setTabOrder(self.txtDefeito, self.txtSolucao)
        TelaNovaOs.setTabOrder(self.txtSolucao, self.txtValor)
        TelaNovaOs.setTabOrder(self.txtValor, self.btnCadastrar)

    def retranslateUi(self, TelaNovaOs):
        _translate = QtCore.QCoreApplication.translate
        TelaNovaOs.setWindowTitle(_translate("TelaNovaOs", "Tela Nova Os"))
        self.label.setText(_translate("TelaNovaOs", "Nova Ordem de Serviço"))
        self.label_2.setText(_translate("TelaNovaOs", "Cliente"))
        self.label_3.setText(_translate("TelaNovaOs", "Tipo"))
        self.cmbTipo.setItemText(0, _translate("TelaNovaOs", "Computador"))
        self.cmbTipo.setItemText(1, _translate("TelaNovaOs", "Notebook"))
        self.cmbTipo.setItemText(2, _translate("TelaNovaOs", "Celular"))
        self.cmbTipo.setItemText(3, _translate("TelaNovaOs", "Tablet"))
        self.label_4.setText(_translate("TelaNovaOs", "Marca"))
        self.label_5.setText(_translate("TelaNovaOs", "Modelo"))
        self.label_6.setText(_translate("TelaNovaOs", "N°Serie"))
        self.label_7.setText(_translate("TelaNovaOs", "Defeito"))
        self.label_8.setText(_translate("TelaNovaOs", "Solução"))
        self.label_9.setText(_translate("TelaNovaOs", "Valor"))
        self.btnCadastrar.setText(_translate("TelaNovaOs", "Cadastrar"))
import resource_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TelaNovaOs = QtWidgets.QMainWindow()
    ui = Ui_TelaNovaOs()
    ui.setupUi(TelaNovaOs)
    TelaNovaOs.show()
    sys.exit(app.exec_())
