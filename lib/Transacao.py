from datetime import datetime

class Transacao:

    DEPOSITO = 0
    SAQUE = 1

    def __init__(self, valor):
        self.__data = datetime.now().date()
        self.__valor = valor

    @property
    def valor(self):
        return self.__valor
    
    @property
    def data(self):
        return self.__data