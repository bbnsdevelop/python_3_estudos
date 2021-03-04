#!/usr/bin/python
# coding: utf-8

from carro import Carro


def main():
    carros = []
    gol = Carro('wolksvagem', 'preto', 15000, 'GOL geração 4', 2)
    gol_4 = Carro('wolksvagem', 'preto', 15000, 'GOL geração 4', 4)
    corsa = Carro('chevrolet', 'preto', 18000, 'Classic', 4)
    corsa_4 = Carro('chevrolet', 'preto', 18000, 'Corsa hatch', 2)

    carros.append(gol)
    carros.append(gol_4)
    carros.append(corsa)
    carros.append(corsa_4)

    # com lambda não funcionou, verificar
    #map(calcular_15_porcento, list(filter(lambda c: c.get_qtd_portas() == 4, carros)))
    #teste = list(filter(lambda c: c.get_qtd_portas() == 4, carros))

    for carro in carros:
        if carro.get_qtd_portas() == 4:
            calcular_15_porcento(carro)
        exibirCarro(carro)


def calcular_15_porcento(carro):
    novoValor = ((carro.get_valor() * 15) / 100) + carro.get_valor()
    carro.set_valor(novoValor)


def exibirCarro(carro):
    carro.exbir()


main()
