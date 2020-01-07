# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TelaInicio.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Main(object):
    def setupUi(self, Main):
        Main.setObjectName("Main")
        Main.resize(740, 487)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Icone/logo-icone.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Main.setWindowIcon(icon)
        Main.setStyleSheet("background-color: \'dodgerblue\';")
        self.centralwidget = QtWidgets.QWidget(Main)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.gridLayout.addItem(spacerItem, 2, 1, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setStyleSheet("image: url(:/Logo/logo.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 1, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 2, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 1, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.gridLayout.addItem(spacerItem3, 0, 1, 1, 1)
        Main.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Main)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 740, 22))
        self.menubar.setStyleSheet("background-color: rgb(85, 87, 83);\n"
"font: 75 12pt \"Nimbus Sans\";\n"
"selection-background-color: rgb(136, 138, 133);\n"
"color: rgb(238, 238, 236);")
        self.menubar.setObjectName("menubar")
        self.menuCliente = QtWidgets.QMenu(self.menubar)
        self.menuCliente.setObjectName("menuCliente")
        self.menuOrdem_de_Servi_o = QtWidgets.QMenu(self.menubar)
        self.menuOrdem_de_Servi_o.setObjectName("menuOrdem_de_Servi_o")
        self.menuAjuda = QtWidgets.QMenu(self.menubar)
        self.menuAjuda.setObjectName("menuAjuda")
        Main.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Main)
        self.statusbar.setObjectName("statusbar")
        Main.setStatusBar(self.statusbar)
        self.menuCadastraCliente = QtWidgets.QAction(Main)
        self.menuCadastraCliente.setObjectName("menuCadastraCliente")
        self.menuBuscarCliente = QtWidgets.QAction(Main)
        self.menuBuscarCliente.setObjectName("menuBuscarCliente")
        self.menuNovaOs = QtWidgets.QAction(Main)
        self.menuNovaOs.setObjectName("menuNovaOs")
        self.menuBucarOs = QtWidgets.QAction(Main)
        self.menuBucarOs.setObjectName("menuBucarOs")
        self.menuSobre = QtWidgets.QAction(Main)
        self.menuSobre.setObjectName("menuSobre")
        self.menuCliente.addAction(self.menuCadastraCliente)
        self.menuCliente.addAction(self.menuBuscarCliente)
        self.menuOrdem_de_Servi_o.addAction(self.menuNovaOs)
        self.menuOrdem_de_Servi_o.addAction(self.menuBucarOs)
        self.menuAjuda.addAction(self.menuSobre)
        self.menubar.addAction(self.menuCliente.menuAction())
        self.menubar.addAction(self.menuOrdem_de_Servi_o.menuAction())
        self.menubar.addAction(self.menuAjuda.menuAction())

        self.retranslateUi(Main)
        QtCore.QMetaObject.connectSlotsByName(Main)

    def retranslateUi(self, Main):
        _translate = QtCore.QCoreApplication.translate
        Main.setWindowTitle(_translate("Main", "Sistema Ordem de Serviço"))
        self.menuCliente.setTitle(_translate("Main", "Cliente"))
        self.menuOrdem_de_Servi_o.setTitle(_translate("Main", "Ordem de Serviço"))
        self.menuAjuda.setTitle(_translate("Main", "Ajuda"))
        self.menuCadastraCliente.setText(_translate("Main", "Cadastro de Cliente"))
        self.menuBuscarCliente.setText(_translate("Main", "Busca de Cliente"))
        self.menuNovaOs.setText(_translate("Main", "Nova OS"))
        self.menuBucarOs.setText(_translate("Main", "Buscar OS"))
        self.menuSobre.setText(_translate("Main", "Sobre"))
import resource_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Main = QtWidgets.QMainWindow()
    ui = Ui_Main()
    ui.setupUi(Main)
    Main.show()
    sys.exit(app.exec_())
