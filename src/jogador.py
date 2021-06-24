
class Jogador():

    def __init__(self, cartas, turno):
        self.cartas = cartas;
        self.turno = turno;
        self.pontuacao = 20;
        self.cartaDaVez = 0;

    def mudançaTurno(self):
        self.turno = not self.turno