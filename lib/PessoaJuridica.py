from lib.Cliente import Cliente
from datetime import date

class PessoaJuridica(Cliente):

    def __init__(self, endereco:str, cnpj:str, nome:str, data_de_registro:date):
        self.__cnpj = cnpj
        self.__nome = nome
        self.__data_de_registro = data_de_registro
        super().__init__(endereco)

    @property
    def cnpj(self):
        return self.__cnpj
    
    @property
    def nome(self):
        return self.__nome
    
    @property
    def data_de_registro(self):
        return self.__data_de_registro
    
    def __str__(self):
        return f'{self.__cnpj} - {self.__nome} - {self.data_de_registro} - {super().endereco}'