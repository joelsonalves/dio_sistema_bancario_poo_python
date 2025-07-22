from lib.Conta import Conta
from lib.Saque import Saque

class ContaEspecial(Conta):

    def __init__(self, agencia:int, numero: int, limite_de_cheque_especial:float, limite_de_saque:int):
        self.__limite_de_cheque_especial = limite_de_cheque_especial
        self.__limite_de_saque = limite_de_saque
        super().__init__(agencia, numero)

    def exibir_saldo(self):
        print(f'Agência: {str(super().numero).zfill(4)}')
        print(f'Conta: {str(super().numero).zfill(8)}')
        print(f'\nCheque especial: {self.__limite_de_cheque_especial:0.2f}')
        print(f'Saldo: {super().saldo + self.__limite_de_cheque_especial:0.2f}\n')

    def exibir_extrato(self):
        print(f'Agência: {str(super().numero).zfill(4)}')
        print(f'Conta: {str(super().numero).zfill(8)}\n')

        super().historico.listar_transacoes() # type: ignore

        print(f'\nCheque especial: {self.__limite_de_cheque_especial:0.2f}')
        print(f'Saldo: {super().saldo + self.__limite_de_cheque_especial:0.2f}\n')

    def sacar(self, valor):
        if super().verificar_quantidade_de_saques_realizados_hoje() < self.__limite_de_saque:
            if super().saldo + self.__limite_de_cheque_especial >= valor:
                saque = Saque(valor)
                super().historico.adicionar_transacao(saque)
                super().deduzir_do_saldo(valor=valor)
            else:
                print('\nSaque não permitido\n')
        else:
            print('\nVocê alcançou o limite diário de saque\n')

    def __str__(self):
        return f'{str(super().agencia).zfill(4)} - {str(super().numero).zfill(8)} - Conta Especial'