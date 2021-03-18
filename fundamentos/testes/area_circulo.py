#!/usr/bin/python
# coding: utf-8

from math import pi
import sys


class TerminalColor:
    COLOR_ERRO = '\033[91m'
    COLOR_NORMAL = '\033[0m'


def circulo(raioDigitado):
    raio = pi * (raioDigitado ** 2)
    return raio


def help_area(msg, erro):
    print(TerminalColor.COLOR_ERRO + msg.format(erro) + TerminalColor.COLOR_NORMAL)
    sys.exit(1)


if __name__ == '__main__':
    try:
        if len(sys.argv) > 1:
            raio = float(sys.argv[1])
            area = circulo(raio)
            print('Área do círculo é: {:.2f}'.format(area))
        elif len(sys.argv) == 1:
            help_area('Você esqueceu de passar o argumento. help: {} <raio>', sys.argv[0][2:])
    except Exception as e:
        help_area('Você tem certeza que digitou um número!! erro {}', e)
