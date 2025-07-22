from lib.Cliente import Cliente
from datetime import date

class PessoaFisica(Cliente):

    def __init__(self, endereco:str, cpf:str, nome:str, data_de_nascimento:date):
        self.__cpf = cpf
        self.__nome = nome
        self.__data_de_nascimento = data_de_nascimento
        super().__init__(endereco)

    @property
    def cpf(self):
        return self.__cpf
    
    @property
    def nome(self):
        return self.__nome
    
    @property
    def data_de_nascimento(self):
        return self.__data_de_nascimento
    
    def __str__(self):
        return f'{self.__cpf} - {self.__nome} - {self.data_de_nascimento} - {super().endereco}'