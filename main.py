from ConfiLogin import *


class Main( ConfiLogin):
    def __init__(self):
        super(ConfiLogin, self).__init__()
        self.setupUi(self)
        tela = QtWidgets.QMainWindow()
        tela.ui = ConfiLogin()
        tela.ui.show()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Main()
    ui.show()
    sys.exit(app.exec_())
