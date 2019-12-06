from PyQt5 import QtCore, QtGui, QtWidgets
from Classes.Mensagem import *
from TelaBuscarCliente import *
from Classes.Cliente import *


class ConfiBuscarCliente(QtWidgets.QMainWindow, Ui_BuscarCliente):


    def __init__(self):
        super(ConfiBuscarCliente, self).__init__()
        self.setupUi(self)
        self.btnBuscar.clicked.connect(self.buscarClientes)
        self.btnAlterar.clicked.connect(self.alterarCliente)
        self.m = Mensagem()

    def buscarClientes(self):
        c = Cliente()

        self.dados = ""
        cpf = c.limpaMask(self.txtCpf.text())
        if cpf != "":
            self.dados = c.buscauser(cpf)
            if self.dados:
                end = str(self.dados[5]).split('-')
                self.ativarComponentes()
                self.txtNome.setText(self.dados[1])
                self.txtCpf.setText(self.dados[2])
                self.txtTel.setText(self.dados[3])
                self.txtCel.setText(self.dados[4])
                self.txtRua.setText(end[0])
                self.txtNum.setText(end[1])
                self.txtBairro.setText(self.dados[6])
                self.txtCidade.setText(self.dados[7])
                self.cmbUF.findText(self.dados[8])
                self.txtCep.setText(self.dados[9])
            else:
                self.m.mensagem_erro("Erro", "Não existe esse CPF cadastrado")
        else:
            self.m.mensagem_erro("Erro", "Insira um CPF para a busca")

    def alterarCliente(self):
        confirmacao = self.m.confirmacao("Confirmação", "Deseja alterar os dados desse cliente?")
        if confirmacao:
            id = self.dados[0]
            nome = self.txtNome.text()
            cpf = self.txtCpf.text()
            tel = self.txtTel.text()
            cel = self.txtCel.text()
            rua = self.txtRua.text() + '-' + self.txtNum.text()
            bairro = self.txtBairro.text()
            cidade = self.txtCidade.text()
            uf = self.cmbUF.currentText()
            cep = self.txtCep.text()
            c = Cliente()
            c.inserirdadosid(id, nome, cpf, tel, cel, rua, bairro, cidade, uf, cep)
            result = c.alterarcliente()
            if result:
                self.limpaCampos()
                self.ativarComponentes()
                self.txtCpf.setCursorPosition(0)
                self.m.mensagem("Sucesso", "Dados Alterado com sucesso!")
            else:
                self.m.mensagem_erro("Erro", "Não foi possivel alterar os dados, contate um administrador se o erro persistir!")

    def ativarComponentes(self):
        self.txtNome.setEnabled(not self.txtNome.isEnabled())
        self.txtTel.setEnabled(not self.txtTel.isEnabled())
        self.txtCel.setEnabled(not self.txtCel.isEnabled())
        self.txtRua.setEnabled(not self.txtRua.isEnabled())
        self.txtNum.setEnabled(not self.txtNum.isEnabled())
        self.txtBairro.setEnabled(not self.txtBairro.isEnabled())
        self.txtCidade.setEnabled(not self.txtCidade.isEnabled())
        self.cmbUF.setEnabled(not self.cmbUF.isEnabled())
        self.txtCep.setEnabled(not self.txtCep.isEnabled())
        self.btnBuscar.setEnabled(not self.btnBuscar.isEnabled())
        self.btnAlterar.setEnabled(not self.btnAlterar.isEnabled())

    def limpaCampos(self):
        self.txtNome.setText("")
        self.txtCpf.setText("")
        self.txtTel.setText("")
        self.txtCel.setText("")
        self.txtRua.setText("")
        self.txtNum.setText("")
        self.txtBairro.setText("")
        self.txtCidade.setText("")
        self.txtCep.setText("")


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    ui = ConfiBuscarCliente()
    ui.show()
    sys.exit(app.exec_())
