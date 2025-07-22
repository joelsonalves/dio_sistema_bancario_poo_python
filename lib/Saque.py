from lib.Transacao import Transacao

class Saque(Transacao):

    def __init__(self, valor):
        super().__init__(valor)