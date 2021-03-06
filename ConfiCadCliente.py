from TelaCadCliente import *
from Classes.Mensagem import Mensagem
from Classes.Cliente import Cliente


class ConfiCadCliente(QtWidgets.QMainWindow, Ui_CadastroCliente):
    def __init__(self):
        super(ConfiCadCliente, self).__init__()
        self.setupUi(self)
        self.btnCadastrar.clicked.connect(self.btnCadCliente)
        self.m = Mensagem()


    def btnCadCliente(self):
        confirm = self.m.confirmacao("Confirmação", "Deseja Cadastrar esse Cliente?")
        if confirm:
            c = Cliente()
            nome = self.txtNome.text()
            cpf = c.limpaMask(self.txtCpf.text())
            tel = c.limpaMask(self.txtTel.text())
            cel = c.limpaMask(self.txtCel.text())
            rua = self.txtRua.text() + '-' + c.limpaMask(self.txtNum.text())
            bairro = self.txtBairro.text()
            cidade = self.txtCidade.text()
            estado = self.cmbUF.currentText()
            cep = self.txtCep.text()
            c.inserirdados(nome, cpf, tel, cel, rua, bairro, cidade, estado, cep)
            result = c.caduser()
            if result:
                self.limpaCampos()
                self.m.mensagem("Sucesso","Cliente Cadastrado com sucesso!")
            else:
                self.m.mensagem_erro("ERRO", "Não foi possivel cadastrar se o erro persistir contate um administrador")

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
    ui = ConfiCadCliente()
    ui.show()
    sys.exit(app.exec_())
