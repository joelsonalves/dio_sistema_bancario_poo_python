from lib.Conta import Conta
from lib.ContaEspecial import ContaEspecial
from lib.Transacao import Transacao

class Cliente:

    PESSOA_FISICA = 0
    PESSOA_JURIDICA = 1

    def __init__(self, endereco:str):
        self.__endereco = endereco
        self.__contas = list()

    @property
    def endereco(self):
        return self.__endereco
    
    @property
    def contas(self):
        return self.__contas
    
    def adicionar_conta_comum(self, agencia:int, numero: int):
        conta = Conta(agencia, numero)
        self.__contas.append(conta)
        return conta

    def adicionar_conta_especial(self, agencia:int, numero: int, limite_de_cheque_especial:float, limite_de_saque:int):
        conta = ContaEspecial(agencia, numero, limite_de_cheque_especial, limite_de_saque)
        self.__contas.append(conta)
        return conta

    def __str__(self):
        return f'{self.__endereco}'