from TelaInicio import *
from ConfiCadCliente import *
from ConfiBuscarCliente import *
from ConfiNovaOs import *
from ConfiSobre import *


class ConfiInicio(QtWidgets.QMainWindow, Ui_Main):
    def __init__(self):
        # super serve para não deixar o metodo construtor sobreescrever os metodos construtor das classes herdadas
        super(ConfiInicio, self).__init__()
        self.setupUi(self)
        self.showMaximized()
        self.menuCadastraCliente.triggered.connect(self.cadcliente)
        self.menuBuscarCliente.triggered.connect(self.buscacliente)
        self.menuNovaOs.triggered.connect(self.telanovaos)
        self.menuSobre.triggered.connect(self.telasobre)

    def cadcliente(self):
        tela = QtWidgets.QDialog(self)
        tela.ui = ConfiCadCliente()
        tela.ui.show()

    def buscacliente(self):
        tela =QtWidgets.QDialog(self)
        tela.ui = ConfiBuscarCliente()
        tela.ui.show()

    def telanovaos(self):
        tela = QtWidgets.QDialog(self)
        tela.ui = ConfiNovaOs()
        tela.ui.show()

    def telasobre(self):
        tela = QtWidgets.QDialog(self)
        tela.ui = ConfiSobre()
        tela.ui.show()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = ConfiInicio()
    ui.show()
    sys.exit(app.exec_())
