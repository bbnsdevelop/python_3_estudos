#!/usr/bin/python
# coding: utf-8

from math import pi


def circulo(raioDigitado):
    raio = pi * (raioDigitado ** 2)
    print('Área do círculo é: {:.2f}'.format(raio))


if __name__ == '__main__':
    raio1 = float(input('Informe o raio: '))
    circulo(raio1)
