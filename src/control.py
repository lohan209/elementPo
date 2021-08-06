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
        self.carta1.clicked.connect(lambda: self.Jogador1.definirCarta(1, self.carta1))
        self.carta2.clicked.connect(lambda: self.Jogador1.definirCarta(2, self.carta2))
        self.carta3.clicked.connect(lambda: self.Jogador1.definirCarta(3, self.carta3))
        self.carta4.clicked.connect(lambda: self.Jogador1.definirCarta(4, self.carta4))
        self.carta5.clicked.connect(lambda: self.Jogador1.definirCarta(5, self.carta5))
        self.carta6.clicked.connect(lambda: self.Jogador2.definirCarta(6, self.carta6))
        self.carta7.clicked.connect(lambda: self.Jogador2.definirCarta(7, self.carta7))
        self.carta8.clicked.connect(lambda: self.Jogador2.definirCarta(8, self.carta8))
        self.carta9.clicked.connect(lambda: self.Jogador2.definirCarta(9, self.carta9))
        self.carta10.clicked.connect(lambda: self.Jogador2.definirCarta(10, self.carta10))

        #Botões de ação das cartas
        self.pos_1.clicked.connect(lambda: self.Jogador1.definirCampo(1, self.campoDeJogo, 0))
        self.pos_2.clicked.connect(lambda: self.Jogador1.definirCampo(1, self.campoDeJogo, 1))
        self.pos_3.clicked.connect(lambda: self.Jogador1.definirCampo(1, self.campoDeJogo, 2))
        self.pos_4.clicked.connect(lambda: self.Jogador1.definirCampo(1, self.campoDeJogo, 3))
        self.pos_5.clicked.connect(lambda: self.Jogador1.definirCampo(1, self.campoDeJogo, 4))
        self.pos_6.clicked.connect(lambda: self.Jogador1.definirCampo(1, self.campoDeJogo, 5))
        self.pos_7.clicked.connect(lambda: self.Jogador1.definirCampo(1, self.campoDeJogo, 6))
        self.pos_8.clicked.connect(lambda: self.Jogador1.definirCampo(1, self.campoDeJogo, 7))
        self.pos_9.clicked.connect(lambda: self.Jogador1.definirCampo(1, self.campoDeJogo, 8))

        self.pos_1_J2.clicked.connect(lambda: self.Jogador2.definirCampo(2, self.campoDeJogo, 0))
        self.pos_2_J2.clicked.connect(lambda: self.Jogador2.definirCampo(2, self.campoDeJogo, 1))
        self.pos_3_J2.clicked.connect(lambda: self.Jogador2.definirCampo(2, self.campoDeJogo, 2))
        self.pos_4_J2.clicked.connect(lambda: self.Jogador2.definirCampo(2, self.campoDeJogo, 3))
        self.pos_5_J2.clicked.connect(lambda: self.Jogador2.definirCampo(2, self.campoDeJogo, 4))
        self.pos_6_J2.clicked.connect(lambda: self.Jogador2.definirCampo(2, self.campoDeJogo, 5))
        self.pos_7_J2.clicked.connect(lambda: self.Jogador2.definirCampo(2, self.campoDeJogo, 6))
        self.pos_8_J2.clicked.connect(lambda: self.Jogador2.definirCampo(2, self.campoDeJogo, 7))
        self.pos_9_J2.clicked.connect(lambda: self.Jogador2.definirCampo(2, self.campoDeJogo, 8))

        self.estadoJogo = gamestate.GameState(False, 0)
        self.Jogador1 = None;
        self.Jogador2 = None;
        self.cartasDoJogo = None;

        self.campoDeJogo = campovelha.Campo()

        self.acaoBtn.clicked.connect(self.threadRun)

    #CONTROLE DAS REGRAS DO JOGO
    def threadRun(self): #running threads
        self.is_running = True
        t = threading.Thread(target=self.iniciarjogo, name="start")
        t.start()

    def preparacaoMaos(self):
        divisaoCartas = self.cartasDoJogo.embaralhar(self.Jogador1, self.Jogador2) #Iniciar partida - # Divisao de cartas

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

    def redistribuicaoCarta(self):
        self.estadoJogo.contadorTurno = 0;
        self.Jogador1.cartas = []
        self.Jogador2.cartas = []
        self.preparacaoMaos()
        self.habilitarBotoes()
        print(self.Jogador1.cartas)
        print(self.Jogador2.cartas)

    def habilitarCampo(self, jogadorDaVez):
        #verificar se a carta escolhida é o jogador 1 ou 2, para definir qual será o próximo turno
        if jogadorDaVez == 1:
            self.esconderCartas1()
            self.mostrarCampo(1, self.campoDeJogo)

        else:
            self.esconderCartas2()
            self.mostrarCampo(2, self.campoDeJogo)

    def estadoInicial(self): #iniciar partida
        self.UI_inicial() #Preparar interface para início do jogo
        self.estadoJogo = gamestate.GameState(True, 0) #Alterar estado do jogo para "Em andamento"
        self.Jogador1 = jogador.Jogador([], True) #Criar jogador 1 e jogador 2
        self.Jogador2 = jogador.Jogador([], False) #Criar jogador 1 e jogador 2
        self.cartasDoJogo = cartas.Baralho() #Criar baralho
        self.alterarBtnAcao(0) #Alterar botão inicial para botão de ação de passar a vez
        self.preparacaoMaos() #Seleção aleatória de 10 cartas
        self.campoDeJogo = campovelha.Campo() #Criar o campo da velha

    def iniciarjogo(self):
        if self.estadoJogo.andamentoJogo == False: #iniciar partida - Verificar se o jogo está em andamento
            self.estadoInicial() #iniciar partida

        else:
            #verificar de quem é a ver
            if self.Jogador1.turno == True: #Iniciar jogada
                self.statusBtnAcao(False) #Iniciar jogada
                self.esconderCartas2() #Iniciar jogada
                self.mostrarCartas1() #Iniciar jogada

                # Aguardando o usuário 1 escolher carta, campo e passar o turno
                while self.Jogador1.cartaDaVez.elemento == "": #Escolher carta
                    continue #Escolher carta

                #habilitar campo de escolha do jogador 1
                self.habilitarCampo(1) #Escolher carta

                # Aguardando jogador 1 selecionar um campo
                while self.Jogador1.campoSelecionado == -1: #Escolher campo
                    continue #Escolher campo

                # Marcar o campo que foi preenchido pelo jogador 1 para que o jogador 2 possa ver
                self.colorirCampo(1, self.Jogador1.campoSelecionado) #Escolher campo

                #verificar se há batalha em campo
                codigoVencedor = self.campoDeJogo.verificarBatalhaCampo(self.Jogador1.campoSelecionado) #Escolher campo

                #verificar se há vencedor da batalha
                if codigoVencedor != 404: #Escolher campo
                    self.marcarVencedorBatalha(self.campoDeJogo.posicoesOcupadas[self.Jogador1.campoSelecionado], self.Jogador1.campoSelecionado) #Escolher campo - Verificar batalha

                #alterar o turno do jogador 1 para o 2
                self.estadoJogo.mudancaTurno(self.Jogador1, self.Jogador2) #Escolher campo

                #zerar o campo escolhido e a carta escolhida pelo jogador 1
                self.Jogador1.reinicioJogada() #Escolher campo

                #alteração de interface para finalizar jogada do jogador 1.
                self.jogada_J1() #Escolher campo

            else:
                self.statusBtnAcao(False)
                self.esconderCartas1() #Iniciar jogada
                self.mostrarCartas2()

                # Aguardando o usuário 2 escolher carta;
                while self.Jogador2.cartaDaVez.elemento == "":
                    continue

                #mostrando o campo para o jogador 2
                self.habilitarCampo(2)

                #aguardando jogador escolher o cmapo;
                while self.Jogador2.campoSelecionado == -1:
                    continue

                #pintar campo de azul para demarcar que tem peça lá
                self.colorirCampo(2, self.Jogador2.campoSelecionado)

                #verificar se há batalha em campo
                codigoVencedor = self.campoDeJogo.verificarBatalhaCampo(self.Jogador2.campoSelecionado)

                if codigoVencedor != 404:
                    self.marcarVencedorBatalha(self.campoDeJogo.posicoesOcupadas[self.Jogador2.campoSelecionado], self.Jogador2.campoSelecionado)

                #alterar o turno
                self.estadoJogo.mudancaTurno(self.Jogador2, self.Jogador1)

                #zerar o campo escolhido e a carta escolhida pelo jogador 1
                self.Jogador2.reinicioJogada()

                #esconder o campo do jogador 2 e habilitar botão de ação
                self.jogada_J2()

            self.estadoJogo.aumentarTurno()

            if self.estadoJogo.contadorTurno == 11: #Iniciar jogada
                self.redistribuicaoCarta()

            #FAZ VERIFICAÇÃO DE VITÓRIA DE JOGO
            self.estadoJogo.definicaoVencedor = self.campoDeJogo.verificarVitoria() #Escolher campo - verificacao vitoria

            if self.estadoJogo.definicaoVencedor != 0:
                self.vitoriaPartida(self.estadoJogo.definicaoVencedor)
                self.estadoJogo.finalizarJogo()