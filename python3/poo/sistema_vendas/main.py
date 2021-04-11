#!/usr/bin/python3
# coding: utf-8

from poo.sistema_vendas.vendas import Vendedor, Cliente, Comprar
from datetime import datetime


def main():
    vendedor_1 = Vendedor('João', 33, 1800)
    vendedor_2 = Vendedor('Tião', 23, 1500)
    compra_1 = Comprar(vendedor_1, datetime.now(), 1200)
    compra_2 = Comprar(vendedor_2, datetime.now(), 1500)
    cliente_1 = Cliente('Marcio', 17)
    cliente_1.registrar_compra(compra_1)
    cliente_1.registrar_compra(compra_2)
    print(f'Cliente: {cliente_1}')
    print(f'Total das compras: R${cliente_1.total_compras()}')
    print(f'Data última compra: {cliente_1.get_data_ultima_compra()}')
    print(f'É adulto: {cliente_1.is_adulto()}')

    for compra in cliente_1.compras:
        print(compra)


if __name__ == '__main__':
    main()
