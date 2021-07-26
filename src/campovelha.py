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

    def analisePosicoes(self):
        print("Entrou na analisePosicoes")

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

        # verificando horizontal 3
        elif self.posicoesOcupadas[2] == 1 and self.posicoesOcupadas[4] == 1 and self.posicoesOcupadas[6] == 1:
            return (1)
        elif self.posicoesOcupadas[2] == 2 and self.posicoesOcupadas[4] == 2 and self.posicoesOcupadas[6] == 2:
            return (2)

        #verificando velha
        else:
            count = 0

            while count < 9:
                if self.posicoesOcupadas[count] != 0:
                    count = count + 1
                else:
                    break

            if count == 9:
                return (3)

            print("Saindo do loop")