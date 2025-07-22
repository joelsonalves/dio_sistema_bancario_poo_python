from lib.PessoaFisica import PessoaFisica
from lib.PessoaJuridica import PessoaJuridica
from datetime import date
import re

class Banco:

    LIMITE_DE_CHEQUE_ESPECIAL_PADRAO = 1_000.0
    LIMITE_DE_SAQUE_PADRAO = 3
    AGENCIA_PADRAO = 1

    __tipo_de_menu = {
        'cliente': {
            '1': 'Cadastrar pessoa física',
            '2': 'Cadastrar pessoa júridica',
            '3': 'Localizar cliente',
            'E': 'Encerrar',
        },
        'conta': {
            '1': 'Abrir conta comum',
            '2': 'Abrir conta especial',
            '3': 'Selecionar conta',
            'V': 'Voltar',
        },
        'operacoes': {
            '1': 'Exibir saldo',
            '2': 'Exibir extrato',
            '3': 'Depositar',
            '4': 'Sacar',
            'V': 'Voltar',
        },
    }

    def __init__(self, nome):
        self.__nome = nome
        self.__clientes = list()
        self.__numero_de_contas = 0
        self.__cliente_selecionado = None
        self.__conta_selecionada = None

    def cliente_ja_foi_cadastrado_anteriormente(self, cpf_cnpj):
        for cliente in self.__clientes:
            if type(cliente) is PessoaFisica:
                if cliente.cpf == cpf_cnpj:
                    return True
            elif type(cliente) is PessoaJuridica:
                if cliente.cnpj == cpf_cnpj:
                    return True
        return False

    def __exibir_menu(self, tipo):
        print('#' * (len(self.__nome) + 8))
        print(f'### {self.__nome.upper()} ###')
        print('#' * (len(self.__nome) + 8))

        print('\nMENU\n')

        if tipo in self.__tipo_de_menu.keys():
            for chave, valor in self.__tipo_de_menu[tipo].items():
                print(f'{chave}: {valor}')

    def run(self):

        # SELEÇÃO DE CLIENTE
        while True:

            self.__exibir_menu(tipo='cliente')

            opcao = input('\nDigite a opção desejada: ').strip().upper()

            print('')

            if opcao == 'E':

                break 

            elif opcao == '1':

                cpf = ''
                while not re.match(pattern=r'^\d{11}$', string=cpf):
                    cpf = input('Digite o CPF: ')
                nome = ''

                if self.cliente_ja_foi_cadastrado_anteriormente(cpf_cnpj=cpf):
                    print('\nCliente já cadastrado anteriormente\n')
                    print('')
                    continue

                while not re.match(pattern=r'^([a-zA-Z]+\s)+[a-zA-Z]+$', string=nome):
                    nome = input('Digite o nome da pessoa: ')
                data_de_nascimento = None
                while not data_de_nascimento:
                    ano_de_nascimento = ''
                    while not re.match(pattern=r'^\d{4}$', string=ano_de_nascimento):
                        ano_de_nascimento = input('Digite o ano de nascimento (AAAA): ')
                    mes_de_nascimento = ''
                    while not re.match(pattern=r'^\d{2}$', string=mes_de_nascimento):
                        mes_de_nascimento = input('Digite o mês de nascimento (MM): ')
                    dia_de_nascimento = ''
                    while not re.match(pattern=r'^\d{2}$', string=dia_de_nascimento):
                        dia_de_nascimento = input('Digite o dia de nascimento (DD): ')
                    try:
                        data_de_nascimento = date(
                            year=int(ano_de_nascimento), 
                            month=int(mes_de_nascimento),
                            day=int(dia_de_nascimento),
                        )
                    except:
                        continue
                    break
                endereco = ''
                while not re.match(pattern=r'^([\w,\-\.:]+\s)+[\w,\-\.:]+$', string=endereco):
                    endereco = input('Digite o endereço: ')
                cliente = PessoaFisica(
                    endereco=endereco,
                    cpf=cpf,
                    nome=nome,
                    data_de_nascimento=data_de_nascimento,
                )
                self.__cliente_selecionado = cliente
                self.__clientes.append(cliente)

            elif opcao == '2':
                cnpj = ''
                while not re.match(pattern=r'^\d{14}$', string=cnpj):
                    cnpj = input('Digite o CNPJ: ')

                if self.cliente_ja_foi_cadastrado_anteriormente(cpf_cnpj=cnpj):
                    print('\nCliente já cadastrado anteriormente\n')
                    print('')
                    continue

                nome = ''
                while not re.match(pattern=r'^([a-zA-Z]+\s)+[a-zA-Z]+$', string=nome):
                    nome = input('Digite o nome da empresa: ')
                data_de_registro = None
                while not data_de_registro:
                    ano_de_registro = ''
                    while not re.match(pattern=r'^\d{4}$', string=ano_de_registro):
                        ano_de_registro = input('Digite o ano de registro (AAAA): ')
                    mes_de_registro = ''
                    while not re.match(pattern=r'^\d{2}$', string=mes_de_registro):
                        mes_de_registro = input('Digite o mês de registro (MM): ')
                    dia_de_registro = ''
                    while not re.match(pattern=r'^\d{2}$', string=dia_de_registro):
                        dia_de_registro = input('Digite o dia de registro (DD): ')
                    try:
                        data_de_registro = date(
                            year=int(ano_de_registro), 
                            month=int(mes_de_registro),
                            day=int(dia_de_registro),
                        )
                    except:
                        continue
                    break
                endereco = ''
                while not re.match(pattern=r'^([\w,\-\.:]+\s)+[\w,\-\.:]+$', string=endereco):
                    endereco = input('Digite o endereço: ')
                cliente = PessoaJuridica(
                    endereco=endereco,
                    cnpj=cnpj,
                    nome=nome,
                    data_de_registro=data_de_registro,
                )
                self.__cliente_selecionado = cliente
                self.__clientes.append(cliente)

            elif opcao == '3':

                cpf_cnpj = ''
                while not re.match(pattern=r'^(\d{11}|\d{14})$', string=cpf_cnpj):
                    cpf_cnpj = input('Digite o CPF/CNPJ: ')

                self.__cliente_selecionado = None

                for cliente in self.__clientes:
                    if type(cliente) is PessoaFisica:
                        if cliente.cpf == cpf_cnpj:
                            self.__cliente_selecionado = cliente
                            break
                    elif type(cliente) is PessoaJuridica:
                        if cliente.cnpj == cpf_cnpj:
                            self.__cliente_selecionado = cliente
                            break
                
                if self.__cliente_selecionado:
                    print(self.__cliente_selecionado)
                else:
                    print('\nCliente não localizado\n')
            
            else:
                print('\nOpção inválida\n')

            print('\n=======\n')

            if self.__cliente_selecionado:

                # SELEÇÃO DE CONTA
                while True:
                
                    self.__exibir_menu(tipo='conta')

                    opcao = input('\nDigite a opção desejada: ').strip().upper()

                    print('')

                    if opcao == 'V':

                        break 

                    elif opcao == '1':

                        
                        self.__conta_selecionada = self.__cliente_selecionado.adicionar_conta_comum(
                            agencia=Banco.AGENCIA_PADRAO,
                            numero=self.__numero_de_contas + 1,
                        ) # type: ignore
                        self.__numero_de_contas += 1

                    elif opcao == '2':

                        self.__conta_selecionada = self.__cliente_selecionado.adicionar_conta_especial(
                            agencia=Banco.AGENCIA_PADRAO,
                            numero=self.__numero_de_contas + 1,
                            limite_de_cheque_especial=Banco.LIMITE_DE_CHEQUE_ESPECIAL_PADRAO,
                            limite_de_saque=Banco.LIMITE_DE_SAQUE_PADRAO,
                        ) # type: ignore
                        self.__numero_de_contas += 1

                    elif opcao == '3':

                        if self.__cliente_selecionado.contas:

                            self.__conta_selecionada = None

                            for i, conta in enumerate(self.__cliente_selecionado.contas): # type: ignore
                                print(f'{i+1}: {conta}')

                            print('')

                            try:        
                                index = int(input('Digite o index da conta desejada: '))
                            except:
                                index = 0

                            if index > 0 and index <= len(self.__cliente_selecionado.contas): # type: ignore
                                self.__conta_selecionada = self.__cliente_selecionado.contas[index - 1] # type: ignore
                            else:
                                print('\nConta não localizada\n')

                        else:
                            print('\nNão há contas cadastradas para o cliente\n')

                    else:
                        print('\nOpção inválida\n')
                    
                    print('\n=======\n')

                    if self.__cliente_selecionado and self.__conta_selecionada:

                        # Operações na conta
                        while True:
                            print('')
                            print(self.__cliente_selecionado)
                            print('')
                            print(self.__conta_selecionada)
                            print('')

                            self.__exibir_menu(tipo='operacoes')

                            opcao = input('\nDigite a opção desejada: ').strip().upper()

                            print('')

                            if opcao == 'V':

                                break 

                            elif opcao == '1':

                                self.__conta_selecionada.exibir_saldo()

                            elif opcao == '2':

                                self.__conta_selecionada.exibir_extrato()

                            elif opcao == '3':

                                print('')

                                valor = ''
                                while not re.match(pattern=r'^\d+([\.\,]{1}\d{1,2})?$', string=valor):
                                    valor = input('Digite o valor a ser depositado em R$: ')
                                valor = re.sub(pattern=',', repl='.', string=valor)

                                self.__conta_selecionada.depositar(valor=float(valor))
                                print('')
                                self.__conta_selecionada.exibir_saldo()

                            elif opcao == '4':

                                print('')
                                
                                valor = ''
                                while not re.match(pattern=r'^\d+([\.\,]{1}\d{1,2})?$', string=valor):
                                    valor = input('Digite o valor a ser sacado em R$: ')
                                valor = re.sub(pattern=',', repl='.', string=valor)
                                
                                self.__conta_selecionada.sacar(valor=float(valor))
                                print('')
                                self.__conta_selecionada.exibir_saldo()

                            else:
                                print('\nOpção inválida\n')

                            print('\n=======\n')
