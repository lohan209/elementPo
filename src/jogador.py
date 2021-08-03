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
            self.cartaDaVez = self.cartas[cartaEscolhida - 1]

        else:
            self.cartaDaVez = self.cartas[cartaEscolhida - 6]

        cartaRemover.setEnabled(False) #desabilitar botão que representa a carta das opções

    def definirCampo(self, jogadorDaVez, campo, pos):
        if jogadorDaVez == 1:
            campo.posicoesJ1[pos].elemento = self.cartaDaVez.elemento
            campo.posicoesJ1[pos].level = self.cartaDaVez.level
            self.campoSelecionado = pos

        else:
            campo.posicoesJ2[pos].elemento = self.cartaDaVez.elemento
            campo.posicoesJ2[pos].level = self.cartaDaVez.level
            self.campoSelecionado = pos