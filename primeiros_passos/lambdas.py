#!/usr/bin/python
# coding: utf-8


square = lambda num: num ** 2

print('Raiz quadrada {}'.format(square(2)))


isPar = lambda x: x % 2 == 0

numeros = [1,2,3,4,5,6,7,8]

for numero in numeros:
    if isPar(numero):
        print('{} é par'.format(numero))