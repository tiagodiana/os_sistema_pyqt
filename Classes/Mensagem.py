from PyQt5.QtWidgets import QMessageBox


class Mensagem():
    def __init__(self):
        pass

    def confirmacao(self,titulo,mensagem):
        q = QMessageBox()
        q.setWindowTitle(titulo)
        q.setText(mensagem)
        q.setIcon(QMessageBox.Question)
        q.setStandardButtons(QMessageBox.Ok|QMessageBox.Cancel)
        x = q.exec_()
        if x == 1024:
                return True
        else:
                return False

    def mensagem(self, titulo, msg):
        q = QMessageBox()
        q.setWindowTitle(titulo)
        q.setText(msg)
        q.setIcon(QMessageBox.Information)
        q.setStandardButtons(QMessageBox.Ok)
        q.exec()


    def mensagem_erro(self, titulo, msg):
        q = QMessageBox()
        q.setWindowTitle(titulo)
        q.setText(msg)
        q.setIcon(QMessageBox.Critical)
        q.setStandardButtons(QMessageBox.Ok)
        q.exec()
