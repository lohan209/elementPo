import sys

import gamestate
import view
from PyQt5 import QtWidgets, QtCore
import cartas
import threading
import jogador

class Control(QtWidgets.QWidget, view.Ui_ElementPo):

    def __init__(self, parent=None):
        super(Control, self).__init__(parent)
        self.setupUi(self)
        #alteração de nome dos botões
        self._translate = QtCore.QCoreApplication.translate

        #Botões de ação das cartas
        self.carta1.clicked.connect(lambda: self.definirJogada(1, self.carta1))
        self.carta2.clicked.connect(lambda: self.definirJogada(2, self.carta2))
        self.carta3.clicked.connect(lambda: self.definirJogada(3, self.carta3))
        self.carta4.clicked.connect(lambda: self.definirJogada(4, self.carta4))
        self.carta5.clicked.connect(lambda: self.definirJogada(5, self.carta5))
        self.carta6.clicked.connect(lambda: self.definirJogada(6, self.carta6))
        self.carta7.clicked.connect(lambda: self.definirJogada(7, self.carta7))
        self.carta8.clicked.connect(lambda: self.definirJogada(8, self.carta8))
        self.carta9.clicked.connect(lambda: self.definirJogada(9, self.carta9))
        self.carta10.clicked.connect(lambda: self.definirJogada(10, self.carta10))

        self.estadoJogo = None;
        self.Jogador1 = None;
        self.Jogador2 = None;
        self.cartasDoJogo = None;

        self.iniciarJogo.clicked.connect(self.threadRun)

    #CONTROLE DAS REGRAS DO JOGO
    def threadRun(self): #running threads
        self.is_running = True
        t = threading.Thread(target=self.jogo, name="start")
        t.start()

    def dividirCartas(self):
        divisaoCartas = self.cartasDoJogo.embaralhar()

        self.carta1.setText(self._translate("Vazio", divisaoCartas[0].elemento+', '+str(divisaoCartas[0].level)))
        self.carta2.setText(self._translate("Vazio", divisaoCartas[1].elemento+', '+str(divisaoCartas[1].level)))
        self.carta3.setText(self._translate("Vazio", divisaoCartas[2].elemento+', '+str(divisaoCartas[2].level)))
        self.carta4.setText(self._translate("Vazio", divisaoCartas[3].elemento+', '+str(divisaoCartas[3].level)))
        self.carta5.setText(self._translate("Vazio", divisaoCartas[4].elemento+', '+str(divisaoCartas[4].level)))
        self.carta6.setText(self._translate("Vazio", divisaoCartas[5].elemento+', '+str(divisaoCartas[5].level)))
        self.carta7.setText(self._translate("Vazio", divisaoCartas[6].elemento+', '+str(divisaoCartas[6].level)))
        self.carta8.setText(self._translate("Vazio", divisaoCartas[7].elemento+', '+str(divisaoCartas[7].level)))
        self.carta9.setText(self._translate("Vazio", divisaoCartas[8].elemento+', '+str(divisaoCartas[8].level)))
        self.carta10.setText(self._translate("Vazio", divisaoCartas[9].elemento+', '+str(divisaoCartas[9].level)))

        i = 0
        while i < 5:
            self.Jogador1.cartas.append(divisaoCartas[i])
            i = i +1;

        while i < 10:
            self.Jogador2.cartas.append(divisaoCartas[i])
            i = i + 1;

    def definirJogada(self, cartaEscolhida, cartaRemover):
        #verificar se a carta escolhida é o jogador 1 ou 2, para definir qual será o próximo turno
        if cartaEscolhida <= 5:
            self.Jogador1.cartaDaVez = self.Jogador1.cartas[cartaEscolhida - 1]
            self.Jogador2.mudançaTurno()
            self.Jogador1.mudançaTurno()

            self.esconderCartas1()
            self.mostrarCartas2()

        else:
            self.Jogador2.cartaDaVez = self.Jogador2.cartas[cartaEscolhida - 6]

            self.label.setText(self._translate(self.label.text(), self.Jogador1.cartaDaVez.elemento+", "+str(self.Jogador1.cartaDaVez.level)))
            self.label_2.setText(self._translate(self.label_2.text(), self.Jogador2.cartaDaVez.elemento+", "+str(self.Jogador2.cartaDaVez.level)))

            self.Jogador2.mudançaTurno()
            self.Jogador1.mudançaTurno()

        cartaRemover.setEnabled(False) #desabilitar botão que representa a carta das opções

    def verificarJogada(self):
        #declarando elemento e level carta jogador 1
        elementoCarta1 = self.Jogador1.cartaDaVez.elemento
        levelCarta1 = self.Jogador1.cartaDaVez.level

        #declarando elemento e level carta jogador 2
        elementoCarta2 = self.Jogador2.cartaDaVez.elemento
        levelCarta2 = self.Jogador2.cartaDaVez.level

        #multiplicando carta jogador 1
        if (elementoCarta2 == "Fogo" and elementoCarta1 == "Agua") or (elementoCarta2 == "Terra" and elementoCarta1 == "Ar") or (elementoCarta2 == "Ar" and elementoCarta1 == "Fogo") or (elementoCarta2 == "Agua" and elementoCarta1 == "Terra"):
            levelCarta1 = levelCarta1 * 2

        #multiplicação do LEVEL da carta do jogador 2
        elif (elementoCarta1 == "Terra" and elementoCarta2 == "Ar") or (elementoCarta1 == "Agua" and elementoCarta2 == "Terra") or (elementoCarta1 == "Ar" and elementoCarta2 == "Fogo") or (elementoCarta1 == "Fogo" and elementoCarta2 == "Agua"):
            levelCarta2 = levelCarta2 * 2

        #verificação de nível
        if levelCarta1 > levelCarta2:
            self.Jogador2.pontuacao = self.Jogador2.pontuacao - (levelCarta1-levelCarta2)

        elif levelCarta2 > levelCarta1:
            self.Jogador1.pontuacao = self.Jogador1.pontuacao - (levelCarta2-levelCarta1)

        else:
            print("Empate")

        #zerando a carta da vez pois finalizou a jogada
        self.Jogador1.cartaDaVez = cartas.Cartas("", 0)
        self.Jogador2.cartaDaVez = cartas.Cartas("", 0)

        self.ponto_Jogador1.setText(self._translate(self.ponto_Jogador1.text(), str(self.Jogador1.pontuacao)))
        self.pontos_Jogador2.setText(self._translate(self.pontos_Jogador2.text(), str(self.Jogador2.pontuacao)))

        #verificando se há pontuação 0
        if self.Jogador1.pontuacao <= 0 or self.Jogador2.pontuacao <= 0:
            self.estadoJogo.andamentoJogo = False

    def verificarVencedor(self):
        # aumenta o turno para finalizar o jogo

        if self.Jogador1.pontuacao == self.Jogador2.pontuacao:
            return "Essa partida foi um empate."

        elif self.Jogador1.pontuacao > self.Jogador2.pontuacao:
            return "Vitória Jogador 1"

        else:
            return "Vitória Jogador 2"

    def estadoInicial(self):
        self.estadoJogo = gamestate.GameState(True, 0)
        self.Jogador1 = jogador.Jogador([], True)
        self.Jogador2 = jogador.Jogador([], False)
        self.cartasDoJogo = cartas.Baralho()

    def jogo(self):
        self.estadoInicial()

        #Dividir as cartas por jogadores
        self.dividirCartas()

        #Alterar VIEW para ficar com UI do início do jogo
        self.inicioJogo_UI()

        while self.estadoJogo.andamentoJogo == True and self.estadoJogo.contadorTurno < 10:

            #não foi definido o vencedor, necessário reembaralhar
            if self.estadoJogo.contadorTurno == 5:
                self.Jogador1.cartas = []
                self.Jogador2.cartas = []
                self.dividirCartas()
                self.habilitarBotoes()

            self.esconderCartas2()
            self.mostrarCartas1()

            #vez do jogador 1
            while self.Jogador1.turno == True:
                continue

            #vez do jogador 2
            while self.Jogador2.turno == True:
                continue

            #aumentar um turno
            self.estadoJogo.aumentarTurno()

            #verificação das jogadas
            self.verificarJogada()

        #remover cartas do jogo
        self.desabilitarBotoes()

        #Escrevendo vencedor
        self.label_3.setText(self._translate(self.label_3.text(), self.verificarVencedor()))

        #Reiniciando interface para nova partida
        self.UI_inicial()