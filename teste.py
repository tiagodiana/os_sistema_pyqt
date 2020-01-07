from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDesktopWidget, QMessageBox



class Second(QtGui):
    def __init__(self, parent=None):
        super(Second, self).__init__(parent)


class First(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(First, self).__init__(parent)
        self.pushButton = QtGui.QPushButton("click me")

        self.setCentralWidget(self.pushButton)

        self.pushButton.clicked.connect(self.on_pushButton_clicked)
        self.dialogs = list()

    def on_pushButton_clicked(self):
        dialog = Second(self)
        self.dialogs.append(dialog)
        dialog.show()


def main():
    app = QtGui.QApplication(sys.argv)
    main = First()
    main.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()