import sys

import gamestate
import view
from PyQt5 import QtWidgets, QtCore
import cartas
import threading
import jogador
import campovelha

class Control(QtWidgets.QWidget, view.Ui_ElementPo):

    def __init__(self, parent=None):
        super(Control, self).__init__(parent)
        self.setupUi(self)
        #alteração de nome dos botões
        self._translate = QtCore.QCoreApplication.translate

        #Botões de ação das cartas
        self.carta1.clicked.connect(lambda: self.definirCarta(1, self.carta1))
        self.carta2.clicked.connect(lambda: self.definirCarta(2, self.carta2))
        self.carta3.clicked.connect(lambda: self.definirCarta(3, self.carta3))
        self.carta4.clicked.connect(lambda: self.definirCarta(4, self.carta4))
        self.carta5.clicked.connect(lambda: self.definirCarta(5, self.carta5))
        self.carta6.clicked.connect(lambda: self.definirCarta(6, self.carta6))
        self.carta7.clicked.connect(lambda: self.definirCarta(7, self.carta7))
        self.carta8.clicked.connect(lambda: self.definirCarta(8, self.carta8))
        self.carta9.clicked.connect(lambda: self.definirCarta(9, self.carta9))
        self.carta10.clicked.connect(lambda: self.definirCarta(10, self.carta10))

        #Botões de ação das cartas
        self.pos_1.clicked.connect(lambda: self.definirCampo(0))
        self.pos_2.clicked.connect(lambda: self.definirCampo(1))
        self.pos_3.clicked.connect(lambda: self.definirCampo(2))
        self.pos_4.clicked.connect(lambda: self.definirCampo(3))
        self.pos_5.clicked.connect(lambda: self.definirCampo(4))
        self.pos_6.clicked.connect(lambda: self.definirCampo(5))
        self.pos_7.clicked.connect(lambda: self.definirCampo(6))
        self.pos_8.clicked.connect(lambda: self.definirCampo(7))
        self.pos_9.clicked.connect(lambda: self.definirCampo(8))

        self.pos_1_J2.clicked.connect(lambda: self.definirCampo(0))
        self.pos_2_J2.clicked.connect(lambda: self.definirCampo(1))
        self.pos_3_J2.clicked.connect(lambda: self.definirCampo(2))
        self.pos_4_J2.clicked.connect(lambda: self.definirCampo(3))
        self.pos_5_J2.clicked.connect(lambda: self.definirCampo(4))
        self.pos_6_J2.clicked.connect(lambda: self.definirCampo(5))
        self.pos_7_J2.clicked.connect(lambda: self.definirCampo(6))
        self.pos_8_J2.clicked.connect(lambda: self.definirCampo(7))
        self.pos_9_J2.clicked.connect(lambda: self.definirCampo(8))

        self.estadoJogo = gamestate.GameState(False, 0)
        self.Jogador1 = None;
        self.Jogador2 = None;
        self.cartasDoJogo = None;

        self.campoDeJogo = campovelha.Campo()

        self.acaoBtn.clicked.connect(self.threadRun)

    #CONTROLE DAS REGRAS DO JOGO
    def threadRun(self): #running threads
        self.is_running = True
        t = threading.Thread(target=self.mudancaEstado, name="start")
        t.start()

    def dividirCartas(self):
        divisaoCartas = self.cartasDoJogo.embaralhar()

        self.carta1.setText(self._translate("Vazio", divisaoCartas[0].elemento+', '+str(divisaoCartas[0].level)))
        self.colocarBgImage(self.carta1, divisaoCartas[0].elemento)
        self.carta2.setText(self._translate("Vazio", divisaoCartas[1].elemento+', '+str(divisaoCartas[1].level)))
        self.colocarBgImage(self.carta2, divisaoCartas[1].elemento)
        self.carta3.setText(self._translate("Vazio", divisaoCartas[2].elemento+', '+str(divisaoCartas[2].level)))
        self.colocarBgImage(self.carta3, divisaoCartas[2].elemento)
        self.carta4.setText(self._translate("Vazio", divisaoCartas[3].elemento+', '+str(divisaoCartas[3].level)))
        self.colocarBgImage(self.carta4, divisaoCartas[3].elemento)
        self.carta5.setText(self._translate("Vazio", divisaoCartas[4].elemento+', '+str(divisaoCartas[4].level)))
        self.colocarBgImage(self.carta5, divisaoCartas[4].elemento)
        self.carta6.setText(self._translate("Vazio", divisaoCartas[5].elemento+', '+str(divisaoCartas[5].level)))
        self.colocarBgImage(self.carta6, divisaoCartas[5].elemento)
        self.carta7.setText(self._translate("Vazio", divisaoCartas[6].elemento+', '+str(divisaoCartas[6].level)))
        self.colocarBgImage(self.carta7, divisaoCartas[6].elemento)
        self.carta8.setText(self._translate("Vazio", divisaoCartas[7].elemento+', '+str(divisaoCartas[7].level)))
        self.colocarBgImage(self.carta8, divisaoCartas[7].elemento)
        self.carta9.setText(self._translate("Vazio", divisaoCartas[8].elemento+', '+str(divisaoCartas[8].level)))
        self.colocarBgImage(self.carta9, divisaoCartas[8].elemento)
        self.carta10.setText(self._translate("Vazio", divisaoCartas[9].elemento+', '+str(divisaoCartas[9].level)))
        self.colocarBgImage(self.carta10, divisaoCartas[9].elemento)

        i = 0
        while i < 5:
            self.Jogador1.cartas.append(divisaoCartas[i])
            i = i +1;

        while i < 10:
            self.Jogador2.cartas.append(divisaoCartas[i])
            i = i + 1;

    def definirCarta(self, cartaEscolhida, cartaRemover):
        #verificar se a carta escolhida é o jogador 1 ou 2, para definir qual será o próximo turno
        if cartaEscolhida <= 5:
            self.Jogador1.cartaDaVez = self.Jogador1.cartas[cartaEscolhida - 1]
            self.esconderCartas1()
            self.mostrarCampo(1, self.campoDeJogo)

        else:
            self.Jogador2.cartaDaVez = self.Jogador2.cartas[cartaEscolhida - 6]
            self.esconderCartas2()
            self.mostrarCampo(2, self.campoDeJogo)

        cartaRemover.setEnabled(False) #desabilitar botão que representa a carta das opções

    def definirCampo(self, pos):
        if self.Jogador1.turno == True:
            self.campoDeJogo.posicoesJ1[pos].elemento = self.Jogador1.cartaDaVez.elemento
            self.campoDeJogo.posicoesJ1[pos].level = self.Jogador1.cartaDaVez.level

            self.preencherCampo(1, pos)

            self.estadoJogo.mudancaTurno(self.Jogador1, self.Jogador2)
            self.jogada_J1()

        else:
            self.campoDeJogo.posicoesJ2[pos].elemento = self.Jogador2.cartaDaVez.elemento
            self.campoDeJogo.posicoesJ2[pos].level = self.Jogador2.cartaDaVez.level

            self.preencherCampo(2, pos)

            self.estadoJogo.mudancaTurno(self.Jogador2, self.Jogador1)
            self.jogada_J2()

        self.verificarBatalhaCampo(pos)

    def verificarBatalhaCampo(self, pos):
        if self.campoDeJogo.posicoesJ1[pos].elemento != "" and self.campoDeJogo.posicoesJ2[pos].elemento != "":
            self.verificarJogada(pos)

    def verificarJogada(self, pos):
        #declarando elemento e level carta jogador 1
        elementoCarta1 = self.campoDeJogo.posicoesJ1[pos].elemento
        levelCarta1 = self.campoDeJogo.posicoesJ1[pos].level

        #declarando elemento e level carta jogador 2
        elementoCarta2 = self.campoDeJogo.posicoesJ2[pos].elemento
        levelCarta2 = self.campoDeJogo.posicoesJ2[pos].level

        #multiplicando carta jogador 1
        if (elementoCarta2 == "Fogo" and elementoCarta1 == "Agua") or (elementoCarta2 == "Terra" and elementoCarta1 == "Ar") or (elementoCarta2 == "Ar" and elementoCarta1 == "Fogo") or (elementoCarta2 == "Agua" and elementoCarta1 == "Terra"):
            levelCarta1 = levelCarta1 * 2

        #multiplicação do LEVEL da carta do jogador 2
        elif (elementoCarta1 == "Terra" and elementoCarta2 == "Ar") or (elementoCarta1 == "Agua" and elementoCarta2 == "Terra") or (elementoCarta1 == "Ar" and elementoCarta2 == "Fogo") or (elementoCarta1 == "Fogo" and elementoCarta2 == "Agua"):
            levelCarta2 = levelCarta2 * 2

        #verificação de nível
        if levelCarta1 > levelCarta2:
            print("O")
            self.marcarVitoriaBatalha(1, pos)
            self.campoDeJogo.posicoesOcupadas[pos] = 1
            self.verificarVitoria()

        elif levelCarta2 > levelCarta1:
            print("X")
            self.marcarVitoriaBatalha(2, pos)
            self.campoDeJogo.posicoesOcupadas[pos] = 2
            self.verificarVitoria()
        else:
            print("Empate")
            self.preencherCampo(3, pos)
            self.campoDeJogo.posicoesJ1[pos] = cartas.Cartas("",0)
            self.campoDeJogo.posicoesJ2[pos] = cartas.Cartas("",0)

        #zerando a carta da vez pois finalizou a jogada
        self.Jogador1.cartaDaVez = cartas.Cartas("", 0)
        self.Jogador2.cartaDaVez = cartas.Cartas("", 0)

    def verificarVitoria(self):
        print(self.campoDeJogo.posicoesOcupadas)

        resultado = self.campoDeJogo.analisePosicoes()

        if resultado == 1:
            self.vitoriaPartida(1)
            self.estadoJogo.finalizarJogo()

        elif resultado == 2:
            self.vitoriaPartida(2)
            self.estadoJogo.finalizarJogo()

        elif resultado == 3:
            self.vitoriaPartida(3)
            self.estadoJogo.finalizarJogo()

        else:
            return False

    def estadoInicial(self):
        self.UI_inicial()
        self.estadoJogo = gamestate.GameState(True, 0)
        self.Jogador1 = jogador.Jogador([], True)
        self.Jogador2 = jogador.Jogador([], False)
        self.cartasDoJogo = cartas.Baralho()
        self.alterarBtnAcao(0)
        self.dividirCartas()
        # self.colocarBgImage(self.cartasDoJogo)
        self.campoDeJogo = campovelha.Campo()

    def mudancaEstado(self):
        if self.estadoJogo.andamentoJogo == False:
            self.estadoInicial()

        else:
            #verificar de quem é a ver
            if self.Jogador1.turno == True:
                self.statusBtnAcao(False)
                self.esconderCartas2()
                self.mostrarCartas1()

                # Aguardando o usuário 1 escolher carta, campo e passar o turno
                while self.Jogador1.turno == True:
                    continue

            else:
                self.mostrarCartas2()
                self.statusBtnAcao(False)

                #Aguardando o usuário 2 escolher carta, campo e passar o turno
                while self.Jogador2.turno == True:
                    continue

        #realizar o aumento de turno após jogada do jogador 2
        self.estadoJogo.aumentarTurno()

        if self.estadoJogo.contadorTurno == 10:
            self.Jogador1.cartas = []
            self.Jogador2.cartas = []
            self.dividirCartas()
            self.habilitarBotoes()
            print(self.Jogador1.cartas)
            print(self.Jogador2.cartas)