# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'element.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ElementPo(object):

    def setupUi(self, ElementPo):
        ElementPo.setObjectName("ElementPo")
        ElementPo.resize(659, 450)
        ElementPo.setMaximumSize(QtCore.QSize(659, 800))
        self.carta1 = QtWidgets.QPushButton(ElementPo)
        self.carta1.setGeometry(QtCore.QRect(30, 50, 113, 32))
        self.carta1.setObjectName("carta1")
        self.carta2 = QtWidgets.QPushButton(ElementPo)
        self.carta2.setGeometry(QtCore.QRect(30, 100, 113, 32))
        self.carta2.setObjectName("carta2")
        self.carta3 = QtWidgets.QPushButton(ElementPo)
        self.carta3.setGeometry(QtCore.QRect(30, 150, 113, 32))
        self.carta3.setObjectName("carta3")
        self.carta4 = QtWidgets.QPushButton(ElementPo)
        self.carta4.setGeometry(QtCore.QRect(30, 200, 113, 32))
        self.carta4.setObjectName("carta4")
        self.carta5 = QtWidgets.QPushButton(ElementPo)
        self.carta5.setGeometry(QtCore.QRect(30, 250, 113, 32))
        self.carta5.setObjectName("carta5")
        self.carta6 = QtWidgets.QPushButton(ElementPo)
        self.carta6.setGeometry(QtCore.QRect(510, 50, 113, 32))
        self.carta6.setObjectName("carta6")
        self.carta7 = QtWidgets.QPushButton(ElementPo)
        self.carta7.setGeometry(QtCore.QRect(510, 100, 113, 32))
        self.carta7.setObjectName("carta7")
        self.carta8 = QtWidgets.QPushButton(ElementPo)
        self.carta8.setGeometry(QtCore.QRect(510, 150, 113, 32))
        self.carta8.setObjectName("carta8")
        self.carta9 = QtWidgets.QPushButton(ElementPo)
        self.carta9.setGeometry(QtCore.QRect(510, 200, 113, 32))
        self.carta9.setObjectName("carta9")
        self.carta10 = QtWidgets.QPushButton(ElementPo)
        self.carta10.setGeometry(QtCore.QRect(510, 250, 113, 32))
        self.carta10.setObjectName("carta10")
        self.label = QtWidgets.QLabel(ElementPo)
        self.label.setGeometry(QtCore.QRect(190, 150, 60, 16))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(ElementPo)
        self.label_2.setGeometry(QtCore.QRect(380, 150, 60, 16))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.ponto_Jogador1 = QtWidgets.QLabel(ElementPo)
        self.ponto_Jogador1.setGeometry(QtCore.QRect(65, 360, 45, 45))
        font = QtGui.QFont()
        font.setPointSize(45)
        self.ponto_Jogador1.setFont(font)
        self.ponto_Jogador1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.ponto_Jogador1.setAlignment(QtCore.Qt.AlignCenter)
        self.ponto_Jogador1.setObjectName("ponto_Jogador1")
        self.pontos_Jogador2 = QtWidgets.QLabel(ElementPo)
        self.pontos_Jogador2.setGeometry(QtCore.QRect(545, 360, 45, 45))
        font = QtGui.QFont()
        font.setPointSize(45)
        self.pontos_Jogador2.setFont(font)
        self.pontos_Jogador2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pontos_Jogador2.setAlignment(QtCore.Qt.AlignCenter)
        self.pontos_Jogador2.setObjectName("pontos_Jogador2")
        self.label_3 = QtWidgets.QLabel(ElementPo)
        self.label_3.setGeometry(QtCore.QRect(10, 330, 631, 20))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.line = QtWidgets.QFrame(ElementPo)
        self.line.setGeometry(QtCore.QRect(37, 300, 571, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.iniciarJogo = QtWidgets.QPushButton(ElementPo)
        self.iniciarJogo.setGeometry(QtCore.QRect(230, 130, 191, 61))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.iniciarJogo.setFont(font)
        self.iniciarJogo.setObjectName("iniciarJogo")

        self.UI_inicial()

        self.retranslateUi(ElementPo)
        QtCore.QMetaObject.connectSlotsByName(ElementPo)


    def UI_inicial(self):
        self.carta1.hide()
        self.carta2.hide()
        self.carta3.hide()
        self.carta4.hide()
        self.carta5.hide()
        self.carta6.hide()
        self.carta7.hide()
        self.carta8.hide()
        self.carta9.hide()
        self.carta10.hide()
        self.label.hide()
        self.label_2.hide()
        self.iniciarJogo.show()
        self.carta1.setEnabled(True)
        self.carta2.setEnabled(True)
        self.carta3.setEnabled(True)
        self.carta4.setEnabled(True)
        self.carta5.setEnabled(True)
        self.carta6.setEnabled(True)
        self.carta7.setEnabled(True)
        self.carta8.setEnabled(True)
        self.carta9.setEnabled(True)
        self.carta10.setEnabled(True)


    def retranslateUi(self, ElementPo):
        _translate = QtCore.QCoreApplication.translate
        ElementPo.setWindowTitle(_translate("ElementPo", "Element PO"))
        self.carta1.setText(_translate("ElementPo", "PushButton"))
        self.carta2.setText(_translate("ElementPo", "PushButton"))
        self.carta3.setText(_translate("ElementPo", "PushButton"))
        self.carta4.setText(_translate("ElementPo", "PushButton"))
        self.carta5.setText(_translate("ElementPo", "PushButton"))
        self.carta6.setText(_translate("ElementPo", "PushButton"))
        self.carta7.setText(_translate("ElementPo", "PushButton"))
        self.carta8.setText(_translate("ElementPo", "PushButton"))
        self.carta9.setText(_translate("ElementPo", "PushButton"))
        self.carta10.setText(_translate("ElementPo", "PushButton"))
        self.label.setText(_translate("ElementPo", "Carta 1"))
        self.label_2.setText(_translate("ElementPo", "Carta 2"))
        self.ponto_Jogador1.setText(_translate("ElementPo", "0"))
        self.pontos_Jogador2.setText(_translate("ElementPo", "0"))
        self.label_3.setText(_translate("ElementPo", "Placar"))
        self.iniciarJogo.setText(_translate("ElementPo", "Iniciar jogo"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ElementPo = QtWidgets.QWidget()
    ui = Ui_ElementPo()
    ui.setupUi(ElementPo)
    ElementPo.show()
    sys.exit(app.exec_())