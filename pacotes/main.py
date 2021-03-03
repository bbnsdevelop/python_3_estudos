#!/usr/bin/python
# coding: utf-8

import math

def raizQuadrada():
    print('Calculando raiz quadrada')
    numero = int(input('Digite um número: '))
    raiz = math.sqrt(numero)
    print('A raiz quadrada é: {}'.format(raiz))

raizQuadrada()
