#!/usr/bin/python
# coding: utf-8

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]

pares = list(filter(lambda a: a % 2 == 0, lista))

print(pares)