# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'element.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ElementPo(object):
    def colocarBgImage(self, carta, elemento):
        if (elemento == "Fogo"):
            carta.setStyleSheet("background-image: url('./fogo.jfif');"
                            "color: #FFF;"
                            "font-weight: bold;")
        elif (elemento == "Agua"):
            carta.setStyleSheet("background-image: url('./agua.jpg');"
                            "color: #FFF;"
                            "font-weight: bold;")
        elif (elemento == "Ar"):
            carta.setStyleSheet("background-image: url('./ar.jpg');"
                            "color: #FFF;"
                            "font-weight: bold;")
        elif (elemento == "Terra"):
            carta.setStyleSheet("background-image: url('./terra.jpg');"
                            "color: #FFF;"
                            "font-weight: bold;")

    def setupUi(self, ElementPo):
        self._translate = QtCore.QCoreApplication.translate

        ElementPo.setObjectName("ElementPo")
        ElementPo.resize(788, 600)
        ElementPo.setMaximumSize(QtCore.QSize(800, 800))
        ElementPo.setAutoFillBackground(False)
        ElementPo.setStyleSheet("")
        self.carta1 = QtWidgets.QPushButton(ElementPo)
        self.carta1.setGeometry(QtCore.QRect(30, 170, 113, 32))
        self.carta1.setObjectName("carta1")
        self.carta2 = QtWidgets.QPushButton(ElementPo)
        self.carta2.setGeometry(QtCore.QRect(30, 220, 113, 32))
        self.carta2.setObjectName("carta2")
        self.carta3 = QtWidgets.QPushButton(ElementPo)
        self.carta3.setGeometry(QtCore.QRect(30, 270, 113, 32))
        self.carta3.setObjectName("carta3")
        self.carta4 = QtWidgets.QPushButton(ElementPo)
        self.carta4.setGeometry(QtCore.QRect(30, 320, 113, 32))
        self.carta4.setObjectName("carta4")
        self.carta5 = QtWidgets.QPushButton(ElementPo)
        self.carta5.setGeometry(QtCore.QRect(30, 370, 113, 32))
        self.carta5.setObjectName("carta5")
        self.carta6 = QtWidgets.QPushButton(ElementPo)
        self.carta6.setGeometry(QtCore.QRect(640, 170, 113, 32))
        self.carta6.setObjectName("carta6")
        self.carta7 = QtWidgets.QPushButton(ElementPo)
        self.carta7.setGeometry(QtCore.QRect(640, 220, 113, 32))
        self.carta7.setObjectName("carta7")
        self.carta8 = QtWidgets.QPushButton(ElementPo)
        self.carta8.setGeometry(QtCore.QRect(640, 270, 113, 32))
        self.carta8.setObjectName("carta8")
        self.carta9 = QtWidgets.QPushButton(ElementPo)
        self.carta9.setGeometry(QtCore.QRect(640, 320, 113, 32))
        self.carta9.setObjectName("carta9")
        self.carta10 = QtWidgets.QPushButton(ElementPo)
        self.carta10.setGeometry(QtCore.QRect(640, 370, 113, 32))
        self.carta10.setObjectName("carta10")
        self.acaoBtn = QtWidgets.QPushButton(ElementPo)
        self.acaoBtn.setGeometry(QtCore.QRect(250, 480, 291, 61))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.acaoBtn.setFont(font)
        self.acaoBtn.setStyleSheet("background-color: rgb(220, 220, 220);")
        self.acaoBtn.setObjectName("acaoBtn")
        self.result_4 = QtWidgets.QLabel(ElementPo)
        self.result_4.setEnabled(True)
        self.result_4.setGeometry(QtCore.QRect(240, 250, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.result_4.setFont(font)
        self.result_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.result_4.setStyleSheet("")
        self.result_4.setAlignment(QtCore.Qt.AlignCenter)
        self.result_4.setObjectName("result_4")
        self.result_5 = QtWidgets.QLabel(ElementPo)
        self.result_5.setEnabled(True)
        self.result_5.setGeometry(QtCore.QRect(360, 250, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.result_5.setFont(font)
        self.result_5.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.result_5.setStyleSheet("")
        self.result_5.setAlignment(QtCore.Qt.AlignCenter)
        self.result_5.setObjectName("result_5")
        self.result_6 = QtWidgets.QLabel(ElementPo)
        self.result_6.setEnabled(True)
        self.result_6.setGeometry(QtCore.QRect(480, 250, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.result_6.setFont(font)
        self.result_6.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.result_6.setStyleSheet("")
        self.result_6.setAlignment(QtCore.Qt.AlignCenter)
        self.result_6.setObjectName("result_6")
        self.result_2 = QtWidgets.QLabel(ElementPo)
        self.result_2.setEnabled(True)
        self.result_2.setGeometry(QtCore.QRect(360, 170, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.result_2.setFont(font)
        self.result_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.result_2.setStyleSheet("")
        self.result_2.setAlignment(QtCore.Qt.AlignCenter)
        self.result_2.setObjectName("result_2")
        self.result_1 = QtWidgets.QLabel(ElementPo)
        self.result_1.setEnabled(True)
        self.result_1.setGeometry(QtCore.QRect(240, 170, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.result_1.setFont(font)
        self.result_1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.result_1.setStyleSheet("")
        self.result_1.setAlignment(QtCore.Qt.AlignCenter)
        self.result_1.setObjectName("result_1")
        self.result_3 = QtWidgets.QLabel(ElementPo)
        self.result_3.setEnabled(True)
        self.result_3.setGeometry(QtCore.QRect(480, 170, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.result_3.setFont(font)
        self.result_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.result_3.setStyleSheet("")
        self.result_3.setAlignment(QtCore.Qt.AlignCenter)
        self.result_3.setObjectName("result_3")
        self.result_8 = QtWidgets.QLabel(ElementPo)
        self.result_8.setEnabled(True)
        self.result_8.setGeometry(QtCore.QRect(360, 330, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.result_8.setFont(font)
        self.result_8.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.result_8.setStyleSheet("")
        self.result_8.setAlignment(QtCore.Qt.AlignCenter)
        self.result_8.setObjectName("result_8")
        self.result_7 = QtWidgets.QLabel(ElementPo)
        self.result_7.setEnabled(True)
        self.result_7.setGeometry(QtCore.QRect(240, 330, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.result_7.setFont(font)
        self.result_7.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.result_7.setStyleSheet("")
        self.result_7.setAlignment(QtCore.Qt.AlignCenter)
        self.result_7.setObjectName("result_7")
        self.result_9 = QtWidgets.QLabel(ElementPo)
        self.result_9.setEnabled(True)
        self.result_9.setGeometry(QtCore.QRect(480, 330, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.result_9.setFont(font)
        self.result_9.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.result_9.setStyleSheet("")
        self.result_9.setAlignment(QtCore.Qt.AlignCenter)
        self.result_9.setObjectName("result_9")
        self.status_jogo = QtWidgets.QLabel(ElementPo)
        self.status_jogo.setGeometry(QtCore.QRect(110, 40, 591, 51))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.status_jogo.setFont(font)
        self.status_jogo.setStyleSheet("")
        self.status_jogo.setAlignment(QtCore.Qt.AlignCenter)
        self.status_jogo.setObjectName("status_jogo")
        self.pos_1 = QtWidgets.QPushButton(ElementPo)
        self.pos_1.setGeometry(QtCore.QRect(230, 170, 91, 81))
        self.pos_1.setText("")
        self.pos_1.setObjectName("pos_1")
        self.pos_2 = QtWidgets.QPushButton(ElementPo)
        self.pos_2.setGeometry(QtCore.QRect(350, 170, 91, 81))
        self.pos_2.setText("")
        self.pos_2.setObjectName("pos_2")
        self.pos_3 = QtWidgets.QPushButton(ElementPo)
        self.pos_3.setGeometry(QtCore.QRect(470, 170, 91, 81))
        self.pos_3.setText("")
        self.pos_3.setObjectName("pos_3")
        self.pos_4 = QtWidgets.QPushButton(ElementPo)
        self.pos_4.setGeometry(QtCore.QRect(230, 250, 91, 81))
        self.pos_4.setText("")
        self.pos_4.setObjectName("pos_4")
        self.pos_5 = QtWidgets.QPushButton(ElementPo)
        self.pos_5.setGeometry(QtCore.QRect(350, 250, 91, 81))
        self.pos_5.setText("")
        self.pos_5.setObjectName("pos_5")
        self.pos_6 = QtWidgets.QPushButton(ElementPo)
        self.pos_6.setGeometry(QtCore.QRect(470, 250, 91, 81))
        self.pos_6.setText("")
        self.pos_6.setObjectName("pos_6")
        self.pos_7 = QtWidgets.QPushButton(ElementPo)
        self.pos_7.setGeometry(QtCore.QRect(230, 330, 91, 81))
        self.pos_7.setText("")
        self.pos_7.setObjectName("pos_7")
        self.pos_8 = QtWidgets.QPushButton(ElementPo)
        self.pos_8.setGeometry(QtCore.QRect(350, 330, 91, 81))
        self.pos_8.setText("")
        self.pos_8.setObjectName("pos_8")
        self.pos_9 = QtWidgets.QPushButton(ElementPo)
        self.pos_9.setGeometry(QtCore.QRect(470, 330, 91, 81))
        self.pos_9.setText("")
        self.pos_9.setObjectName("pos_9")

        self.pos_1_J2 = QtWidgets.QPushButton(ElementPo)
        self.pos_1_J2.setGeometry(QtCore.QRect(230, 170, 91, 81))
        self.pos_1_J2.setText("")
        self.pos_1_J2.setObjectName("pos_1")
        self.pos_2_J2 = QtWidgets.QPushButton(ElementPo)
        self.pos_2_J2.setGeometry(QtCore.QRect(350, 170, 91, 81))
        self.pos_2_J2.setText("")
        self.pos_2_J2.setObjectName("pos_2")
        self.pos_3_J2 = QtWidgets.QPushButton(ElementPo)
        self.pos_3_J2.setGeometry(QtCore.QRect(470, 170, 91, 81))
        self.pos_3_J2.setText("")
        self.pos_3_J2.setObjectName("pos_3")
        self.pos_4_J2 = QtWidgets.QPushButton(ElementPo)
        self.pos_4_J2.setGeometry(QtCore.QRect(230, 250, 91, 81))
        self.pos_4_J2.setText("")
        self.pos_4_J2.setObjectName("pos_4")
        self.pos_5_J2 = QtWidgets.QPushButton(ElementPo)
        self.pos_5_J2.setGeometry(QtCore.QRect(350, 250, 91, 81))
        self.pos_5_J2.setText("")
        self.pos_5_J2.setObjectName("pos_5")
        self.pos_6_J2 = QtWidgets.QPushButton(ElementPo)
        self.pos_6_J2.setGeometry(QtCore.QRect(470, 250, 91, 81))
        self.pos_6_J2.setText("")
        self.pos_6_J2.setObjectName("pos_6")
        self.pos_7_J2 = QtWidgets.QPushButton(ElementPo)
        self.pos_7_J2.setGeometry(QtCore.QRect(230, 330, 91, 81))
        self.pos_7_J2.setText("")
        self.pos_7_J2.setObjectName("pos_7")
        self.pos_8_J2 = QtWidgets.QPushButton(ElementPo)
        self.pos_8_J2.setGeometry(QtCore.QRect(350, 330, 91, 81))
        self.pos_8_J2.setText("")
        self.pos_8_J2.setObjectName("pos_8")
        self.pos_9_J2 = QtWidgets.QPushButton(ElementPo)
        self.pos_9_J2.setGeometry(QtCore.QRect(470, 330, 91, 81))
        self.pos_9_J2.setText("")
        self.pos_9_J2.setObjectName("pos_9")

        self.carta1.raise_()
        self.carta2.raise_()
        self.carta3.raise_()
        self.carta4.raise_()
        self.carta5.raise_()
        self.carta6.raise_()
        self.carta7.raise_()
        self.carta8.raise_()
        self.carta9.raise_()
        self.carta10.raise_()

        self.acaoBtn.raise_()
        self.result_4.raise_()
        self.result_5.raise_()
        self.result_6.raise_()
        self.result_2.raise_()
        self.result_1.raise_()
        self.result_3.raise_()
        self.result_8.raise_()
        self.result_7.raise_()
        self.result_9.raise_()
        self.status_jogo.raise_()

        self.pos_1.raise_()
        self.pos_2.raise_()
        self.pos_3.raise_()
        self.pos_4.raise_()
        self.pos_5.raise_()
        self.pos_6.raise_()
        self.pos_7.raise_()
        self.pos_8.raise_()
        self.pos_9.raise_()

        self.pos_1_J2.raise_()
        self.pos_2_J2.raise_()
        self.pos_3_J2.raise_()
        self.pos_4_J2.raise_()
        self.pos_5_J2.raise_()
        self.pos_6_J2.raise_()
        self.pos_7_J2.raise_()
        self.pos_8_J2.raise_()
        self.pos_9_J2.raise_()
        self.UI_inicial()

        self.retranslateUi(ElementPo)
        QtCore.QMetaObject.connectSlotsByName(ElementPo)

    def retranslateUi(self, ElementPo):
        _translate = QtCore.QCoreApplication.translate
        ElementPo.setWindowTitle(_translate("ElementPo", "Element PO"))
        self.carta1.setText(_translate("ElementPo", "Vazio"))
        self.carta2.setText(_translate("ElementPo", "Vazio"))
        self.carta3.setText(_translate("ElementPo", "Vazio"))
        self.carta4.setText(_translate("ElementPo", "Vazio"))
        self.carta5.setText(_translate("ElementPo", "Vazio"))
        self.carta6.setText(_translate("ElementPo", "Vazio"))
        self.carta7.setText(_translate("ElementPo", "Vazio"))
        self.carta8.setText(_translate("ElementPo", "Vazio"))
        self.carta9.setText(_translate("ElementPo", "Vazio"))
        self.carta10.setText(_translate("ElementPo", "Vazio"))
        self.acaoBtn.setText(_translate("ElementPo", "Iniciar jogo"))
        self.result_4.setText(_translate("ElementPo", "-"))
        self.result_5.setText(_translate("ElementPo", "-"))
        self.result_6.setText(_translate("ElementPo", "-"))
        self.result_2.setText(_translate("ElementPo", "-"))
        self.result_1.setText(_translate("ElementPo", "-"))
        self.result_3.setText(_translate("ElementPo", "-"))
        self.result_8.setText(_translate("ElementPo", "-"))
        self.result_7.setText(_translate("ElementPo", "-"))
        self.result_9.setText(_translate("ElementPo", "-"))
        self.status_jogo.setText(_translate("ElementPo", "Status da partida"))

    def UI_inicial(self):
        self.acaoBtn.setText(self._translate(self.acaoBtn.text(), "Iniciar jogo"))
        self.status_jogo.setText(self._translate(self.status_jogo.text(), "Status da partida"))

        btnGroup = [self.pos_1, self.pos_2, self.pos_3, self.pos_4, self.pos_5, self.pos_6, self.pos_7, self.pos_8,
                    self.pos_9]
        btnGroup2 = [self.pos_1_J2, self.pos_2_J2, self.pos_3_J2, self.pos_4_J2, self.pos_5_J2, self.pos_6_J2,
                     self.pos_7_J2, self.pos_8_J2, self.pos_9_J2]

        for i in btnGroup:
            i.setStyleSheet("background-color: light gray;")

        for i in btnGroup2:
            i.setStyleSheet("background-color: light gray;")

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
        self.acaoBtn.show()
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
        self.result_1.hide()
        self.result_2.hide()
        self.result_3.hide()
        self.result_4.hide()
        self.result_5.hide()
        self.result_6.hide()
        self.result_7.hide()
        self.result_8.hide()
        self.result_9.hide()

        self.pos_1.hide()
        self.pos_2.hide()
        self.pos_3.hide()
        self.pos_4.hide()
        self.pos_5.hide()
        self.pos_6.hide()
        self.pos_7.hide()
        self.pos_8.hide()
        self.pos_9.hide()
        self.pos_1_J2.hide()
        self.pos_2_J2.hide()
        self.pos_3_J2.hide()
        self.pos_4_J2.hide()
        self.pos_5_J2.hide()
        self.pos_6_J2.hide()
        self.pos_7_J2.hide()
        self.pos_8_J2.hide()
        self.pos_9_J2.hide()

        self.pos_1.setEnabled(True)
        self.pos_2.setEnabled(True)
        self.pos_3.setEnabled(True)
        self.pos_4.setEnabled(True)
        self.pos_5.setEnabled(True)
        self.pos_6.setEnabled(True)
        self.pos_7.setEnabled(True)
        self.pos_8.setEnabled(True)
        self.pos_9.setEnabled(True)
        self.pos_1_J2.setEnabled(True)
        self.pos_2_J2.setEnabled(True)
        self.pos_3_J2.setEnabled(True)
        self.pos_4_J2.setEnabled(True)
        self.pos_5_J2.setEnabled(True)
        self.pos_6_J2.setEnabled(True)
        self.pos_7_J2.setEnabled(True)
        self.pos_8_J2.setEnabled(True)
        self.pos_9_J2.setEnabled(True)

    def esconderCartas1(self):
        self.carta1.hide()
        self.carta2.hide()
        self.carta3.hide()
        self.carta4.hide()
        self.carta5.hide()

    def esconderCartas2(self):
        self.carta6.hide()
        self.carta7.hide()
        self.carta8.hide()
        self.carta9.hide()
        self.carta10.hide()

    def mostrarCartas1(self):
        self.carta1.show()
        self.carta2.show()
        self.carta3.show()
        self.carta4.show()
        self.carta5.show()

    def mostrarCartas2(self):
        self.carta6.show()
        self.carta7.show()
        self.carta8.show()
        self.carta9.show()
        self.carta10.show()

    def desabilitarBotoes(self):
        self.carta1.setEnabled(False)
        self.carta2.setEnabled(False)
        self.carta3.setEnabled(False)
        self.carta4.setEnabled(False)
        self.carta5.setEnabled(False)
        self.carta6.setEnabled(False)
        self.carta7.setEnabled(False)
        self.carta8.setEnabled(False)
        self.carta9.setEnabled(False)
        self.carta10.setEnabled(False)

    def habilitarBotoes(self):
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

    def mostrarCampo(self, jogador, campo):
        btnGroup = [self.pos_1, self.pos_2, self.pos_3, self.pos_4, self.pos_5, self.pos_6, self.pos_7, self.pos_8,
                    self.pos_9]
        btnGroup2 = [self.pos_1_J2, self.pos_2_J2, self.pos_3_J2, self.pos_4_J2, self.pos_5_J2, self.pos_6_J2,
                     self.pos_7_J2, self.pos_8_J2, self.pos_9_J2]
        count = 0;

        if jogador == 1:
            for i in campo.posicoesOcupadas:
                if i == 0:
                    btnGroup[count].show()

                count = count + 1;

        else:
            for i in campo.posicoesOcupadas:
                if i == 0:
                    btnGroup2[count].show()

                count = count + 1;

    def esconderCampo_J1(self):
        self.pos_1.hide()
        self.pos_2.hide()
        self.pos_3.hide()
        self.pos_4.hide()
        self.pos_5.hide()
        self.pos_6.hide()
        self.pos_7.hide()
        self.pos_8.hide()
        self.pos_9.hide()

    def esconderCampo_J2(self):
        self.pos_1_J2.hide()
        self.pos_2_J2.hide()
        self.pos_3_J2.hide()
        self.pos_4_J2.hide()
        self.pos_5_J2.hide()
        self.pos_6_J2.hide()
        self.pos_7_J2.hide()
        self.pos_8_J2.hide()
        self.pos_9_J2.hide()

    #altera o nome do botão de ação para os jogadores conseguirem prosseguir com o jogo
    def alterarBtnAcao(self, tipo):
        _translate = QtCore.QCoreApplication.translate

        if tipo == 1:
            self.acaoBtn.setText(_translate(self.acaoBtn.text(), "Iniciar jogada do J2"))
            self.acaoBtn.setStyleSheet("background-color: rgb(176, 196, 222);")
            self.statusBtnAcao(True)
        else:
            self.acaoBtn.setStyleSheet("background-color: rgb(245, 211, 179);")
            self.acaoBtn.setText(_translate(self.acaoBtn.text(), "Iniciar jogada do J1"))
            self.statusBtnAcao(True)

    #habilita e desabilita o botão ação
    def statusBtnAcao(self, status):
        self.acaoBtn.setEnabled(status)

    def colorirCampo(self, jogador, posCampo):
        btnGroup = [self.pos_1, self.pos_2, self.pos_3, self.pos_4, self.pos_5, self.pos_6, self.pos_7, self.pos_8,
                    self.pos_9]
        btnGroup2 = [self.pos_1_J2, self.pos_2_J2, self.pos_3_J2, self.pos_4_J2, self.pos_5_J2, self.pos_6_J2,
                     self.pos_7_J2, self.pos_8_J2, self.pos_9_J2]

        if jogador == 1:
            #marca o campo para o jogador 2 ver que posicoes estão ocupadas
            btnGroup2[posCampo].setStyleSheet("background-color: rgb(245, 211, 179);")

            #desabilita o campo para o jogador 1 nao poder utilizar mais
            btnGroup[posCampo].setEnabled(False)

        elif jogador == 2:
            #mesma ideia do if acima
            btnGroup[posCampo].setStyleSheet("background-color: rgb(176, 196, 222);")
            btnGroup2[posCampo].setEnabled(False)

        else:
            btnGroup2[posCampo].setStyleSheet("background-color: light gray;")
            btnGroup2[posCampo].setEnabled(True)
            btnGroup[posCampo].setStyleSheet("background-color: light gray;")
            btnGroup[posCampo].setEnabled(True)

    def marcarVencedorBatalha(self, codigoVencedor, posicaoVencedor):
        resultLabelGroup = [self.result_1, self.result_2, self.result_3, self.result_4, self.result_5, self.result_6, self.result_7, self.result_8, self.result_9]

        if codigoVencedor == 1:
            resultLabelGroup[posicaoVencedor].setText(self._translate(resultLabelGroup[posicaoVencedor].text(), "J1"))
            resultLabelGroup[posicaoVencedor].show()
        elif codigoVencedor == 2:
            resultLabelGroup[posicaoVencedor].setText(self._translate(resultLabelGroup[posicaoVencedor].text(), "J2"))
            resultLabelGroup[posicaoVencedor].show()
        else:
            self.preencherCampo(3, posicaoVencedor)

    def vitoriaPartida(self, jogador):

        if jogador == 1:
            self.status_jogo.setText(self._translate(self.status_jogo.text(), "Jogador 1 ganhou!"))
            self.status_jogo.setStyleSheet("background-color: rgb(245, 211, 179);")

        elif jogador == 2:
            self.status_jogo.setText(self._translate(self.status_jogo.text(), "Jogador 2 ganhou!"))
            self.status_jogo.setStyleSheet("background-color: rgb(176, 196, 222);")
        else:
            self.status_jogo.setText(self._translate(self.status_jogo.text(), "Empate!!"))

        self.acaoBtn.setText(self._translate(self.acaoBtn.text(), "Iniciar jogo"))
        self.acaoBtn.setStyleSheet("background-color: light gray;")

    def jogada_J1(self):
        self.alterarBtnAcao(1)
        self.esconderCampo_J1()
        self.alterarLabelStatus(2)

    def jogada_J2(self):
        self.alterarBtnAcao(0)
        self.esconderCampo_J2()
        self.alterarLabelStatus(1)

    def alterarLabelStatus(self, jogadorDaVez):

        self.status_jogo.setText(self._translate(self.status_jogo.text(), "Vez do Jogador " + str(jogadorDaVez)))
        if jogadorDaVez == 1:
            self.status_jogo.setStyleSheet("color: rgb(245, 211, 179);")
        else:
            self.status_jogo.setStyleSheet("color: rgb(176, 196, 222);")
