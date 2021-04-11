#!/usr/bin/python
# coding: utf-8

x = [1, 3, 5, 7, 9]
y = [2, 4, 6, 8, 10]

tupla = list(zip(x, y))

print(tupla)

for n in zip(x, y):
    print(max(n))
