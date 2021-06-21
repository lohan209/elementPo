import sys
import control
import view
from PyQt5 import QtWidgets, QtCore

class Main(QtWidgets.QWidget, view.Ui_ElementPo):

    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        self.setupUi(self)

def main():
    app = QtWidgets.QApplication(sys.argv)
    form = control.Control()
    form.show()
    app.exec_()

if __name__ == '__main__':
    main()
