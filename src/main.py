import sys
import control
from PyQt5 import QtWidgets

def main():
    app = QtWidgets.QApplication(sys.argv)
    form = control.Control()
    form.show()
    app.exec_()

if __name__ == '__main__':
    main()
