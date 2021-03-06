import random

class Cartas():

    def __init__(self, elemento, level):
        self.elemento = elemento
        self.level = level

class Baralho():

    def __init__(self):
        self.baralho = [
            Cartas("Fogo",1),
            Cartas("Fogo", 2),
            Cartas("Fogo", 3),
            Cartas("Fogo", 4),
            Cartas("Fogo", 5),
            Cartas("Agua", 1),
            Cartas("Agua", 2),
            Cartas("Agua", 3),
            Cartas("Agua", 4),
            Cartas("Agua", 5),
            Cartas("Terra", 1),
            Cartas("Terra", 2),
            Cartas("Terra", 3),
            Cartas("Terra", 4),
            Cartas("Terra", 5),
            Cartas("Ar", 1),
            Cartas("Ar", 2),
            Cartas("Ar", 3),
            Cartas("Ar", 4),
            Cartas("Ar", 5)
        ]

    def embaralhar(self, jogador1, jogador2):
        count = 0;
        cartasDoJogo = []

        while count != 10:
            cartasDoJogo.append(self.verificacaoCartasBaralho())
            #posicaoValida = True
            count = count + 1

        self.dividirCartar(jogador1, jogador2, cartasDoJogo)

        return cartasDoJogo

    def verificacaoCartasBaralho(self):
        posicaoValida = True

        while posicaoValida:
            try:
                numCarta = random.randint(0, 19)
                posicaoValida = False
                carta = self.baralho[numCarta]
                del (self.baralho[numCarta])
                return carta
            except:
                posicaoValida = True

    def dividirCartar(self, jogador1, jogador2, cartasDoJogo):
        i = 0
        while i < 5:
            jogador1.cartas.append(cartasDoJogo[i])
            i = i + 1;

        while i < 10:
            jogador2.cartas.append(cartasDoJogo[i])
            i = i + 1;