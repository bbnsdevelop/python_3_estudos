#!/usr/bin/python
# coding: utf-8

from random import randint


def gerar_numero():
    return randint(0, 9)


def executar():
    msg = 'Número gerado foi {}'
    while True:
        num = gerar_numero()
        print(msg.format(num))
        if num == 3:
            break


if __name__ == '__main__':
    executar()
