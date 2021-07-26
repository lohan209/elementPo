class GameState():

    def __init__(self, andamentoJogo, contadorTurno):
        self.andamentoJogo = andamentoJogo;
        self.contadorTurno = contadorTurno;

    def finalizarJogo(self):
        self.andamentoJogo = False;

    def aumentarTurno(self):
        self.contadorTurno = self.contadorTurno + 1;

    def mudancaTurno(self,jogadorCorrente, jogadorOposto):
        jogadorCorrente.turno = not jogadorCorrente.turno
        jogadorOposto.turno = not jogadorOposto.turno