class Comprar:
    def __init__(self, vendedor, data, valor):
        self.vendedor = vendedor
        self.data = data
        self.valor = valor

    def __str__(self):
        return f'Vendendor: {self.vendedor.nome}, Data: {self.data}, Valor: {self.valor}'
