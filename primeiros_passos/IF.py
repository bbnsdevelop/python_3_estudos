#!/usr/bin/env python
# -*- coding: utf-8 -*-

print("""
Programa que verifica
se um número é maior do que outro com IF
""")
num1 = raw_input('Digite um número: ')
num2 = raw_input('Digite outro número: ')

if num1 > num2:
    print('O número: {}, é maior do que {}'.format(num1, num2))
else:
    print('O número: {}, é menor do que {}'.format(num1, num2))