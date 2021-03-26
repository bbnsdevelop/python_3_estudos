#!/usr/bin/python3
# coding: utf-8


def soma(a, b):
    return a +b


def soma_n(*numeros):
    #transforma numeros em uma tupla
    sum_1 = 0
    for n in numeros:
        sum_1 += n
    return sum_1


if __name__ == '__main__':
    print(soma(1, 2))
    print(soma_n(1, 2, 3, 4))


