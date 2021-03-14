#!/usr/bin/python
# coding: utf-8


def maior(num1, num2):
    print('num1 é maior que num2? {}'.format(num1 > num2))


def menor(num1, num2):
    print('num1 é menor que num2? {}'.format(num1 < num2))


def igual(num1, num2):
    print('num1 é igual que num2? {}'.format(num1 == num2))


def diferente(num1, num2):    
    print('num1 é diferente que num2? {}'.format(num1 != num2))


def elevado(num1, num2):
    '''
    params n1,n2
    return n1 ** n2
    '''
    print('num1 é elevado a num2? {}'.format(num1 ** num2))


def modulo(num1, num2):
    print('num1 é resto da divisao que num2? {}'.format(num1 % num2))

def desafio(salario, despesas):
    percentual = (despesas * 100) / salario
    print('A porcentagem que as dispesas tem sobre o salário é: {:.2f}%'.format(percentual))


def main(num1, num2):
    maior(num1, num2)
    menor(num1, num2)
    igual(num1, num2)
    diferente(num1, num2)
    elevado(num1, num2)
    modulo(num1, num2)
    desafio(3450.45, 2456.2)


main(2, 5)
