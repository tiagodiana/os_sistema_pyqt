from TelaNovaOs import *
from Classes.Ordem import *
from Classes.Cliente import *
from Classes.Mensagem import *


class ConfiNovaOs(QtWidgets.QMainWindow, Ui_TelaNovaOs):
    def __init__(self):
        super(ConfiNovaOs, self).__init__()
        self.setupUi(self)
        self.m = Mensagem()
        # Inserindo dados no ComboBox Cliente
        try:
            c = Cliente()
            all_user = c.alluser()
            for c in all_user:
                self.cmbCliente.addItem(c['nome'])

        except:
            self.m.mensagem_erro("ERRO", "Não foi possivel conectar com o servidor!")

        self.btnCadastrar.clicked.connect(self.btncadastrarordem)

    def btncadastrarordem(self):
        confirmacao = self.m.confirmacao("Confirmação", "Deseja Criar essa Ordem de Serviço?")
        if confirmacao:
            c = Ordem()
            cliente = self.cmbCliente.currentText()
            tipo = self.cmbTipo.currentText()
            marca = self.txtMarca.text()
            modelo = self.txtModelo.text()
            num_serie = self.txtNumSerie.text()
            defeito = self.txtDefeito.toPlainText()
            solucao = self.txtSolucao.toPlainText()
            valor = float(self.txtValor.text())
            c.inserindodados_nova(cliente,tipo, marca,modelo , num_serie, defeito, solucao, valor)
            result = c.novaos()
            print(result)
            if result:
                self.m.mensagem("Sucesso", "Ordem de Serviço Criada com Sucesso")
            else:
                self.m.mensagem_erro("Erro", "Não foi possivel Cadastrar")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = ConfiNovaOs()
    ui.show()
    sys.exit(app.exec_())
