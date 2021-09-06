import cartas

class Campo():

    def __init__(self):
        self.posicoesJ1 = [
            cartas.Cartas("", 0),
            cartas.Cartas("", 0),
            cartas.Cartas("", 0),
            cartas.Cartas("", 0),
            cartas.Cartas("", 0),
            cartas.Cartas("", 0),
            cartas.Cartas("", 0),
            cartas.Cartas("", 0),
            cartas.Cartas("", 0)
        ]

        self.posicoesJ2 = [
            cartas.Cartas("", 0),
            cartas.Cartas("", 0),
            cartas.Cartas("", 0),
            cartas.Cartas("", 0),
            cartas.Cartas("", 0),
            cartas.Cartas("", 0),
            cartas.Cartas("", 0),
            cartas.Cartas("", 0),
            cartas.Cartas("", 0)
        ]

        self.posicoesOcupadas = [
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0
        ]

    def inserirCartaCampo(self, pos, elemento, level):
        self.posicoesJ1[pos].elemento = elemento
        self.posicoesJ1[pos].level = level

    def inserirCartaCampo2(self, pos, elemento, level):
        self.posicoesJ2[pos].elemento = elemento
        self.posicoesJ2[pos].level = level

    def analisePosicoes(self):
        #verificando vertical 1
        if self.posicoesOcupadas[0] == 1 and self.posicoesOcupadas[1] == 1 and self.posicoesOcupadas[2] == 1:
            return(1)
        elif self.posicoesOcupadas[0] == 2 and self.posicoesOcupadas[1] == 2 and self.posicoesOcupadas[2] == 2:
            return(2)

        #verificando diagonal 1
        elif self.posicoesOcupadas[0] == 1 and self.posicoesOcupadas[4] == 1 and self.posicoesOcupadas[8] == 1:
            return (1)
        elif self.posicoesOcupadas[0] == 2 and self.posicoesOcupadas[4] == 2 and self.posicoesOcupadas[8] == 2:
            return (2)

        #verificando horizontal 1
        elif self.posicoesOcupadas[0] == 1 and self.posicoesOcupadas[3] == 1 and self.posicoesOcupadas[6] == 1:
            return (1)
        elif self.posicoesOcupadas[0] == 2 and self.posicoesOcupadas[3] == 2 and self.posicoesOcupadas[6] == 2:
            return (2)

        #verificando vertical 2
        elif self.posicoesOcupadas[3] == 1 and self.posicoesOcupadas[4] == 1 and self.posicoesOcupadas[5] == 1:
            return (1)
        elif self.posicoesOcupadas[3] == 2 and self.posicoesOcupadas[4] == 2 and self.posicoesOcupadas[5] == 2:
            return (2)

        #verificando horizontal 2
        elif self.posicoesOcupadas[1] == 1 and self.posicoesOcupadas[4] == 1 and self.posicoesOcupadas[7] == 1:
            return (1)
        elif self.posicoesOcupadas[1] == 2 and self.posicoesOcupadas[4] == 2 and self.posicoesOcupadas[7] == 2:
            return (2)

        # verificando vertical 3
        elif self.posicoesOcupadas[6] == 1 and self.posicoesOcupadas[7] == 1 and self.posicoesOcupadas[8] == 1:
            return (1)
        elif self.posicoesOcupadas[6] == 2 and self.posicoesOcupadas[7] == 2 and self.posicoesOcupadas[8] == 2:
            return (2)

        # verificando horizontal 3
        elif self.posicoesOcupadas[2] == 1 and self.posicoesOcupadas[5] == 1 and self.posicoesOcupadas[8] == 1:
            return (1)
        elif self.posicoesOcupadas[2] == 2 and self.posicoesOcupadas[5] == 2 and self.posicoesOcupadas[8] == 2:
            return (2)

        # verificando diagonal 3
        elif self.posicoesOcupadas[2] == 1 and self.posicoesOcupadas[4] == 1 and self.posicoesOcupadas[6] == 1:
            return (1)
        elif self.posicoesOcupadas[2] == 2 and self.posicoesOcupadas[4] == 2 and self.posicoesOcupadas[6] == 2:
            return (2)

        #verificando velha
        else:
            count = 0
            count2 = 0

            while count < 9:
                if self.posicoesOcupadas[count] != 0:
                    count2 = count2 + 1
                count = count + 1
            if count2 == 9:
                return (3)
            else:
                return (0)

    def verificarBatalhaCampo(self, pos):
        if self.posicoesJ1[pos].elemento != "" and self.posicoesJ2[pos].elemento != "":
            self.verificarJogada(pos)
        else:
            return 404

    def verificarJogada(self, pos): #Escolher campo - Verificar batalha
        #declarando elemento e level carta jogador 1
        elementoCarta1 = self.posicoesJ1[pos].elemento
        levelCarta1 = self.posicoesJ1[pos].level

        #declarando elemento e level carta jogador 2
        elementoCarta2 = self.posicoesJ2[pos].elemento
        levelCarta2 = self.posicoesJ2[pos].level

        #multiplicando carta jogador 1
        if (elementoCarta2 == "Fogo" and elementoCarta1 == "Agua") or (elementoCarta2 == "Terra" and elementoCarta1 == "Ar") or (elementoCarta2 == "Ar" and elementoCarta1 == "Fogo") or (elementoCarta2 == "Agua" and elementoCarta1 == "Terra"):
            levelCarta1 = levelCarta1 * 2

        #multiplicação do LEVEL da carta do jogador 2
        elif (elementoCarta1 == "Terra" and elementoCarta2 == "Ar") or (elementoCarta1 == "Agua" and elementoCarta2 == "Terra") or (elementoCarta1 == "Ar" and elementoCarta2 == "Fogo") or (elementoCarta1 == "Fogo" and elementoCarta2 == "Agua"):
            levelCarta2 = levelCarta2 * 2

        #verificação de nível
        if levelCarta1 > levelCarta2:
            print("Vitória jogador 1")
            print(elementoCarta1+"; "+str(levelCarta1)+" > "+elementoCarta2+"; "+str(levelCarta2))
            self.posicoesOcupadas[pos] = 1
            return int(pos)

        elif levelCarta2 > levelCarta1:
            print("Vitória jogador 2")
            print(elementoCarta2+"; "+str(levelCarta2)+" > "+elementoCarta1+"; "+str(levelCarta1))
            self.posicoesOcupadas[pos] = 2
            return int(pos)

        else:
            print("Empate")
            print(elementoCarta1+"; "+str(levelCarta1)+" = "+elementoCarta2+"; "+str(levelCarta2))
            self.posicoesJ1[pos] = cartas.Cartas("",0)
            self.posicoesJ2[pos] = cartas.Cartas("",0)
            return 400

    def verificarVitoria(self):
        print(self.posicoesOcupadas)

        resultado = self.analisePosicoes()

        if resultado == 1:
            return 1
            self.vitoriaPartida(1)
            self.estadoJogo.finalizarJogo()

        elif resultado == 2:
            return 2
            self.vitoriaPartida(2)
            self.estadoJogo.finalizarJogo()

        elif resultado == 3:
            return 3
            self.vitoriaPartida(3)
            self.estadoJogo.finalizarJogo()

        else:
            return False