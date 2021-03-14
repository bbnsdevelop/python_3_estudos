#!usr/bin/python
# coding: utf-8


def conversao():
    num1 = 5
    num2 = float('6.8')
    result = soma(num1, num2)
    exiba(result)
    num1 = str(num1)
    num2 = str(num2)
    result = soma(num1, num2)
    exiba(result)


def soma(n1, n2):
    return n1 + n2


def exiba(result):
    print('Tipo {}'.format(type(result)))
    print('Soma {}'.format(result))


conversao()
