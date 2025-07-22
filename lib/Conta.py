from lib.Saque import Saque
from lib.Deposito import Deposito
from lib.Historico import Historico

class Conta:

    CONTA_COMUM = 0
    CONTA_ESPECIAL = 1

    def __init__(self, agencia:int, numero: int):
        self.__agencia = agencia
        self.__numero = numero
        self.__historico = Historico()
        self.__saldo = 0.0

    @property
    def agencia(self):
        return self.__agencia
    
    @property
    def numero(self):
        return self.__numero
    
    @property
    def saldo(self):
        return self.__saldo

    @property
    def historico(self):
        return self.__historico
    
    def exibir_saldo(self):
        print(f'Agência: {str(self.__numero).zfill(4)}')
        print(f'Conta: {str(self.__numero).zfill(8)}')
        print(f'\nSaldo: {self.__saldo:0.2f}\n')

    def exibir_extrato(self):
        print(f'Agência: {str(self.__numero).zfill(4)}')
        print(f'Conta: {str(self.__numero).zfill(8)}\n')

        self.__historico.listar_transacoes()

        print(f'\nSaldo: {self.__saldo:0.2f}\n')
    
    def sacar(self, valor):
        if valor > 0 and self.__saldo >= valor:
            saque = Saque(valor)
            self.__historico.adicionar_transacao(saque)
            self.__saldo -= valor
        else:
            print('\nSaque não permitido\n')

    def deduzir_do_saldo(self, valor):
        self.__saldo -= valor

    def depositar(self, valor):
        if valor > 0:
            deposito = Deposito(valor)
            self.__historico.adicionar_transacao(deposito)
            self.__saldo += valor
        else:
            print('\nDepósito inválido\n')

    def verificar_quantidade_de_saques_realizados_hoje(self):
        return self.__historico.verificar_quantidade_de_saques_realizados_hoje()

    def __str__(self):
        return f'{str(self.__agencia).zfill(4)} - {str(self.__numero).zfill(8)} - Conta Comum'