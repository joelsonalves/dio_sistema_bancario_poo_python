from lib.Transacao import Transacao

class Deposito(Transacao):

    def __init__(self, valor):
        super().__init__(valor)