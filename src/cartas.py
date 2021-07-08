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

    def embaralhar(self):
        count = 0;
        verificar = True
        cartasDoJogo = []

        while count != 10:
            while verificar:
                try:
                    numCarta = random.randint(0, 19)
                    verificarCarta = self.baralho[numCarta]
                    verificar = False
                except:
                    verificar = True

            verificar = True
            count = count + 1

            cartasDoJogo.append(self.baralho[numCarta])
            del(self.baralho[numCarta])

        return cartasDoJogo