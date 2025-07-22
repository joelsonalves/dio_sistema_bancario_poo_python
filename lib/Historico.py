from lib.Transacao import Transacao
from lib.Saque import Saque
from lib.Deposito import Deposito
from datetime import datetime

class Historico:

    def __init__(self):
        self.__transacoes = list()

    @property
    def transacoes(self):
        return self.__transacoes

    def adicionar_transacao(self, transacao:Transacao):
        self.__transacoes.append(transacao)

    def verificar_quantidade_de_saques_realizados_hoje(self):
        hoje = datetime.now().date()
        num_saques_hoje = 0
        for transacao in self.__transacoes:
            if type(transacao) is Saque:
                if transacao.data == hoje:
                    num_saques_hoje += 1
        return num_saques_hoje
    
    def listar_transacoes(self):
        for transacao in self.__transacoes:
            if type(transacao) is Deposito:
                print(f'{transacao.data} - R$ {transacao.valor:0.2f} (+)')
            elif type(transacao) is Saque:
                print(f'{transacao.data} - R$ {transacao.valor:0.2f} (-)')