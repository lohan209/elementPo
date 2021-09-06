import cartas

class Jogador():

    def __init__(self, carta, turno):
        self.cartas = carta;
        self.turno = turno;
        self.cartaDaVez = cartas.Cartas("", 0)
        self.campoSelecionado = -1

    def reinicioJogada(self):
        self.campoSelecionado = -1
        self.cartaDaVez = cartas.Cartas("", 0)

    def definirCarta(self, cartaEscolhida, cartaRemover):
        #verificar se a carta escolhida é o jogador 1 ou 2, para definir qual será o próximo turno
        if cartaEscolhida <= 5:
            self.salvarCarta(cartaEscolhida, 1)

        else:
            self.salvarCarta(cartaEscolhida, 6)

        self.desabilitarCarta(cartaRemover) #desabilitar botão que representa a carta das opções

    def salvarCarta(self, cartaEscolhida, intApoio):
        self.cartaDaVez = self.cartas[cartaEscolhida - intApoio]

    def desabilitarCarta(self, cartaRemover):
        cartaRemover.setEnabled(False)

    def definirCampo(self, jogadorDaVez, campo, pos):
        if jogadorDaVez == 1:
            campo.inserirCartaCampo(pos, self.cartaDaVez.elemento, self.cartaDaVez.level)
        else:
            campo.inserirCartaCampo2(pos, self.cartaDaVez.elemento, self.cartaDaVez.level)
        self.campoSelecionado = pos
