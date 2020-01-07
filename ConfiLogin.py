from TelaLogin import *
from ConfiInicio import *
from Classes.Mensagem import *


class ConfiLogin(QtWidgets.QMainWindow, Ui_TelaLogin):
    def __init__(self):
        self.nome = 'root'
        self.senha = 'toor'
        self.m = Mensagem()
        super(ConfiLogin, self).__init__()
        self.setupUi(self)
        self.btnEntrar.clicked.connect(self.btnentrar)

    def btnentrar(self):
        if self.txtUsername.text() != self.nome or self.txtPassword.text() != self.senha:
            self.m.mensagem_erro('Login Incorreto', 'O usuário ou a senha estão incorretos!')
        else:
            self.m.mensagem('Login Correto', 'Bem vindo ao Sistema OS')
            self.close()
            self.telainicio()

    def telainicio(self):
        tela = QtWidgets.QMainWindow(self)
        tela.ui = ConfiInicio()
        tela.ui.show()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = ConfiLogin()
    ui.show()
    sys.exit(app.exec_())
