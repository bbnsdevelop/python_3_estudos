# coding=utf-8

# -*- coding: utf-8 -*-

a = True
b = False
c = True
print(a == b or a == c)

if a == b:
    print(a)
else:
    print(b)

if a == b or a == c:
    print('operador OR deu a condição ' + str(a))
    