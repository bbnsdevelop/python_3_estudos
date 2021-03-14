#!usr/bin/python
# coding: utf-8

from decimal import Decimal, getcontext

num1 = Decimal(1.16)
num2 = Decimal(2.2)
result = num1 + num2

print(result)

getcontext().prec = 3
result = num1 + num2

num2 = result + 5
print('result: {}'.format(result))
print('num1:{:.2f} e num2:{} o maior é: {}'.format(num1, num2, Decimal.max(num1, num2)))
print('maior é: {}'.format(result.max(num2)))
