#!/usr/bin/python
# coding: utf-8

from Circulo import Circulo

def main():
    circulo = Circulo()

    raio = int(input('Digite o raio:'))

    circulo.setRaio(raio)

    print('Calculando a área do raio {}: {}'.format(circulo.getRario(), circulo.area()))

main()