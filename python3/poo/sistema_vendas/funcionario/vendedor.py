from poo.sistema_vendas.pessoa_modulo.pessoa import Pessoa


class Vendedor(Pessoa):
    def __init__(self, nome, idade, salario):
        super().__init__(nome, idade)
        self.salario = salario