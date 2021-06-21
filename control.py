import sys

import gamestate
import view
from PyQt5 import QtWidgets, QtCore
import cartas
import threading
import viewmanagement
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

        self.estadoJogo = gamestate.GameState(True, 0)
        self.Jogador1 = jogador.Jogador([], 1, 0)
        self.Jogador2 = jogador.Jogador([], 0, 0)

        self.iniciarJogo.clicked.connect(self.threadRun)

    #CONTROLE DE UI
    def esconderCartas2(self):
        self.carta6.hide()
        self.carta7.hide()
        self.carta8.hide()
        self.carta9.hide()
        self.carta10.hide()

    def esconderCartas1(self):
        self.carta1.hide()
        self.carta2.hide()
        self.carta3.hide()
        self.carta4.hide()
        self.carta5.hide()

    def mostrarCartas2(self):
        self.carta6.show()
        self.carta7.show()
        self.carta8.show()
        self.carta9.show()
        self.carta10.show()

    def mostrarCartas1(self):
        self.carta1.show()
        self.carta2.show()
        self.carta3.show()
        self.carta4.show()
        self.carta5.show()

    def mostrarCartasEscolhidas(self):
        self.label.show()
        self.label_2.show()

        self.label.setText(self._translate(self.label.text(), "Carta 1"))
        self.label_2.setText(self._translate(self.label_2.text(), "Carta 2"))

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

    def inicioJogo_UI(self):
        self.iniciarJogo.hide()
        self.mostrarCartas1()
        self.mostrarCartasEscolhidas()
        self.label_3.setText(self._translate(self.label_3.text(), "Placar"))
        self.ponto_Jogador1.setText(self._translate(self.ponto_Jogador1.text(), "0"))
        self.pontos_Jogador2.setText(self._translate(self.pontos_Jogador2.text(), "0"))

    #CONTROLE DAS REGRAS DO JOGO
    def threadRun(self): #running threads
        self.is_running = True
        t = threading.Thread(target=self.jogo, name="start")
        t.start()

    def dividirCartas(self):
        self.cartasDoJogo = cartas.Baralho().embaralhar()

        self.carta1.setText(self._translate("Vazio", self.cartasDoJogo[0][0]+', '+str(self.cartasDoJogo[0][1])))
        self.carta2.setText(self._translate("Vazio", self.cartasDoJogo[1][0]+', '+str(self.cartasDoJogo[1][1])))
        self.carta3.setText(self._translate("Vazio", self.cartasDoJogo[2][0]+', '+str(self.cartasDoJogo[2][1])))
        self.carta4.setText(self._translate("Vazio", self.cartasDoJogo[3][0]+', '+str(self.cartasDoJogo[3][1])))
        self.carta5.setText(self._translate("Vazio", self.cartasDoJogo[4][0]+', '+str(self.cartasDoJogo[4][1])))
        self.carta6.setText(self._translate("Vazio", self.cartasDoJogo[5][0]+', '+str(self.cartasDoJogo[5][1])))
        self.carta7.setText(self._translate("Vazio", self.cartasDoJogo[6][0]+', '+str(self.cartasDoJogo[6][1])))
        self.carta8.setText(self._translate("Vazio", self.cartasDoJogo[7][0]+', '+str(self.cartasDoJogo[7][1])))
        self.carta9.setText(self._translate("Vazio", self.cartasDoJogo[8][0]+', '+str(self.cartasDoJogo[8][1])))
        self.carta10.setText(self._translate("Vazio", self.cartasDoJogo[9][0]+', '+str(self.cartasDoJogo[9][1])))

        i = 0
        while i < 5:
            self.Jogador1.cartas.append(self.cartasDoJogo[i])
            i = i +1;

        while i < 10:
            self.Jogador2.cartas.append(self.cartasDoJogo[i])
            i = i + 1;

    def definirJogada(self, cartaEscolhida, cartaRemover):
        #verificar se a carta escolhida é o jogador 1 ou 2, para definir qual será o próximo turno
        if cartaEscolhida <= 5:
            self.Jogador2.mudançaTurno()
            self.Jogador1.mudançaTurno()

            self.mostrarCartas2()
            self.Jogador1.cartaDaVez = self.Jogador1.cartas[cartaEscolhida-1]

        else:
            self.Jogador2.mudançaTurno()
            self.Jogador1.mudançaTurno()

            self.mostrarCartas1()
            self.Jogador2.cartaDaVez = self.Jogador2.cartas[cartaEscolhida-6]


            print(str(self.Jogador1.cartaDaVez))
            print(str(self.Jogador2.cartaDaVez))

            self.label.setText(self._translate(self.label.text(), str(self.Jogador1.cartaDaVez).encode('utf-8')))
            self.label_2.setText(self._translate(self.label_2.text(), str(self.Jogador2.cartaDaVez).encode('utf-8')))

        cartaRemover.setEnabled(False) #desabilitar botão que representa a carta das opções

    def verificarJogada(self):
        pontuacaoAntiga1 = self.Jogador1.pontuacao
        pontuacaoAntiga2 = self.Jogador2.pontuacao


        elementoCarta1 = self.Jogador1.cartaDaVez[0]
        print("elemento carta1: "+elementoCarta1)
        levelCarta1 = self.Jogador1.cartaDaVez[1]
        print("level carta1:"+str(levelCarta1))

        elementoCarta2 = self.Jogador2.cartaDaVez[0]
        print("elemento carta2: "+elementoCarta2)

        levelCarta2 = self.Jogador2.cartaDaVez[1]
        print("level carta2:"+str(levelCarta2))

        #verificação de elemento
        if elementoCarta1 == "Fogo" and elementoCarta2 == "Agua":
            self.Jogador2.pontuacao = self.Jogador2.pontuacao + 1

        elif elementoCarta2 == "Fogo" and elementoCarta1 == "Agua":
            self.Jogador1.pontuacao = self.Jogador1.pontuacao + 1

        elif elementoCarta1 == "Terra" and elementoCarta2 == "Ar":
            self.Jogador2.pontuacao = self.Jogador2.pontuacao + 1

        elif elementoCarta2 == "Terra" and elementoCarta1 == "Ar":
            self.Jogador1.pontuacao = self.Jogador1.pontuacao + 1

        elif elementoCarta1 == "Ar" and elementoCarta2 == "Fogo":
            self.Jogador2.pontuacao = self.Jogador2.pontuacao + 1

        elif elementoCarta2 == "Ar" and elementoCarta1 == "Fogo":
            self.Jogador1.pontuacao = self.Jogador1.pontuacao + 1

        elif elementoCarta1 == "Agua" and elementoCarta2 == "Terra":
            self.Jogador2.pontuacao = self.Jogador2.pontuacao + 1

        elif elementoCarta2 == "Agua" and elementoCarta1 == "Terra":
            self.Jogador1.pontuacao = self.Jogador1.pontuacao + 1

        else:
            #verificação de nível
            if levelCarta1 > levelCarta2:
                self.Jogador1.pontuacao = self.Jogador1.pontuacao + 1

            elif levelCarta2 > levelCarta1:
                self.Jogador2.pontuacao = self.Jogador2.pontuacao + 1
            else:
                print("Empate")

        #zerando a carta da vez pois finalizou a jogada
        self.Jogador1.cartaDaVez = 0
        self.Jogador2.cartaDaVez = 0

        self.ponto_Jogador1.setText(self._translate(str(pontuacaoAntiga1), str(self.Jogador1.pontuacao)))
        self.pontos_Jogador2.setText(self._translate(str(pontuacaoAntiga2), str(self.Jogador2.pontuacao)))

        if self.Jogador1.pontuacao == 3:
            self.estadoJogo.finalizarJogo()
            return ("Jogador 1 ganhou")

        if self.Jogador2.pontuacao == 3:
            self.estadoJogo.finalizarJogo()
            return ("Jogador 2 ganhou")

        return True

    def reinicioJogo(self):
        self.estadoJogo = gamestate.GameState(True, 0)
        self.Jogador1 = jogador.Jogador([], 1, 0)
        self.Jogador2 = jogador.Jogador([], 0, 0)

    def jogo(self):
        #Dividir as cartas por jogadores
        self.dividirCartas()

        #Alterar VIEW para ficar com UI do início do jogo
        self.inicioJogo_UI()

        vencedor = ""

        while self.estadoJogo.andamentoJogo == True and self.estadoJogo.contadorTurno < 5:
            #vez do jogador 1
            self.esconderCartas2()
            while self.Jogador1.turno == 1:
                continue

            #vez do jogador 2
            self.esconderCartas1()
            while self.Jogador2.turno == 1:
                continue

            #verificação das jogadas
            vencedor = self.verificarJogada()

            #aumenta o turno para finalizar o jogo
            self.estadoJogo.aumentarTurno()

        #verificaçãoEmpate
        if self.Jogador1.pontuacao == self.Jogador2:
            vencedor = "Essa partida foi um empate."

        #remover cartas do jogo
        self.desabilitarBotoes()

        #Escrevendo vencedor
        self.label_3.setText(self._translate(self.label_3.text(), vencedor))

        #Reiniciando interface para nova partida
        self.UI_inicial()
        self.reinicioJogo()