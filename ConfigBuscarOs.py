from TelaBuscarOs import *
from Classes.Ordem import *
from Classes.Mensagem import *

class ConfigBuscarOs(QtWidgets.QMainWindow, Ui_TelaBuscarOs):
    def __init__(self):
        super(ConfigBuscarOs, self).__init__()
        self.setupUi(self)
        self.o = Ordem()
        self.m = Mensagem()
        self.txtCliente.setEnabled(False)
        self.btnFinalizar.setEnabled(False)
        self.btnBuscar.clicked.connect(self.buscarordem)
        self.btnAlterar.clicked.connect(self.alterarordem)
        self.btnDeletar.clicked.connect(self.deletarordem)
        self.btnLimpar.clicked.connect(self.limparCampos)
    
    def buscarordem(self):
        num_ordem = self.txtNumOrdem.text()
        self.o.inserirId(num_ordem)
        result = self.o.buscaros()
        if result:
            self.ativaCampos()
            self.txtCliente.setText(result['nome'])
            self.cmbTipo.findText(result['tipo'])
            self.txtMarca.setText(result['marca'])
            self.txtModelo.setText(result['modelo'])
            self.txtNumSerie.setText(result['num_serie'])
            self.txtSolucao.setText(result['solucao'])
            self.txtDefeito.setText(result['defeito'])
            self.txtValor.setText(result['valor'])
        else:
            self.m.mensagem_erro("Erro", "Não foi possivel encontrar essa ordem")
            self.txtNumOrdem.setFocus()

    def alterarordem(self):
        confirmacao = self.m.confirmacao("Confirmação", "Deseja alterar essa ordem de serviço?")
        if confirmacao:
            id_os = self.txtNumOrdem.text()
            tipo = self.cmbTipo.currentText()
            marca = self.txtMarca.text()
            modelo = self.txtModelo.text()
            num_serie = self.txtNumSerie.text()
            defeito = self.txtDefeito.toPlainText()
            solucao = self.txtSolucao.toPlainText()
            valor = self.txtValor.text()
            self.o.inserindodados_alt(id_os, tipo, marca, modelo, num_serie, defeito, solucao, valor)
            result = self.o.alteraros()
            if result:
                self.m.mensagem("Sucesso", "Ordem de Serviço alterada com sucesso")
            else:
                self.m.mensagem_erro("Erro", "Erro não for possível alterar a Ordem de Serviço")

    def deletarordem(self):
        confirmacao = self.m.confirmacao("Confirmação", "Deseja apagar essa ordem de serviço??")
        if confirmacao:
            id_os = self.txtNumOrdem.text()
            self.o.inserirId(id_os)
            result = self.o.deletaros()
            if result:
                self.m.mensagem("Sucesso", "Ordem de Serviço deletada com Sucesso!")
                self.limparCampos()
            else:
                self.m.mensagem_erro("Erro", "Erro ao deletar a Ordem de Serviço")
            

    def ativaCampos(self):
        self.txtNumOrdem.setEnabled(not self.txtNumOrdem.isEnabled())
        self.cmbTipo.setEnabled(not self.cmbTipo.isEnabled())
        self.txtMarca.setEnabled(not self.txtMarca.isEnabled())
        self.txtModelo.setEnabled(not self.txtModelo.isEnabled())
        self.txtNumSerie.setEnabled(not self.txtNumSerie.isEnabled())
        self.txtDefeito.setEnabled(not self.txtDefeito.isEnabled())
        self.txtSolucao.setEnabled(not self.txtSolucao.isEnabled())
        self.txtValor.setEnabled(not self.txtValor.isEnabled())
        self.btnBuscar.setEnabled(not self.btnBuscar.isEnabled())
        self.btnFinalizar.setEnabled(not self.btnFinalizar.isEnabled())
        self.btnAlterar.setEnabled(not self.btnAlterar.isEnabled())
        self.btnDeletar.setEnabled(not self.btnDeletar.isEnabled())
        self.btnLimpar.setEnabled(not self.btnLimpar.isEnabled())

    def limparCampos(self):
        self.ativaCampos()
        self.txtNumOrdem.clear()
        self.txtCliente.clear()
        self.txtMarca.clear()
        self.txtModelo.clear()
        self.txtNumSerie.clear()
        self.txtSolucao.clear()
        self.txtDefeito.clear()
        self.txtValor.clear()








if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = ConfigBuscarOs()
    ui.show()
    sys.exit(app.exec_())

