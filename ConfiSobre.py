from PyQt5 import QtCore, QtGui, QtWidgets
from TelaSobre import *


class ConfiSobre(QtWidgets.QMainWindow, Ui_TelaSobre):
    def __init__(self):
        super(ConfiSobre, self).__init__()
        self.setupUi(self)
        self.btnSair.clicked.connect(lambda: self.close())


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = ConfiSobre()
    ui.show()
    sys.exit(app.exec_())
