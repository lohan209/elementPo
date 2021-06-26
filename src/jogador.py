import cartas

class Jogador():

    def __init__(self, carta, turno):
        self.cartas = carta;
        self.turno = turno;
        self.pontuacao = 20;
        self.cartaDaVez = cartas.Cartas("", 0)

    def mudançaTurno(self):
        self.turno = not self.turno