
class Jogador():

    def __init__(self, cartas, turno, pontuacao):
        self.cartas = cartas;
        self.turno = turno;
        self.pontuacao = pontuacao;
        self.cartaDaVez = 0;

    def mudançaTurno(self):
        self.turno = abs(self.turno - 1)