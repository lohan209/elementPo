import cartas

class Jogador():

    def __init__(self, carta, turno):
        self.cartas = carta;
        self.turno = turno;
        self.cartaDaVez = cartas.Cartas("", 0)

    def mudançaTurno(self, jogadorOposto):
        self.turno = not self.turno
        jogadorOposto.turno = not self.turno