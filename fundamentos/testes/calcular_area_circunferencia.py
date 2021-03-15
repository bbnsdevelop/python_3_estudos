#!/usr/bin/python
# coding: utf-8

import math


def get_pi():
    return math.pi


def get_raio():
    raio = float(input('Digite a área do circulo: '))
    return raio


def main():
    print('Calculando área da cirunferência.')
    raio = get_raio()
    pi = get_pi()

    result = pi * (raio ** 2)
    print('Área do círculo é: {:.2f}'.format(result))


main()
