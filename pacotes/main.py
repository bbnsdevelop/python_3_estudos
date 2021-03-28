#!/usr/bin/python
# coding: utf-8

from p1 import modulo_soma
import math
from p2.modulo_subtracao import subtracao as sub

def raizQuadrada():
    print('Calculando raiz quadrada')
    numero = int(input('Digite um número: '))
    raiz = math.sqrt(numero)
    print('A raiz quadrada é: {}'.format(raiz))


if __name__ == '__main__':
    print(f'A soma é: {modulo_soma.soma(5, 9)}')
    print(f'A subtração de {9}-{5} é: {sub(9, 5)}')
