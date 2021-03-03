#!/usr/bin/python
# coding: utf-8

from functools import reduce

# aplicao uma função em um interavel

lst = [10, 10, 10, 10, 10]

total = reduce(lambda x, y: (x + y), lst) / 5  # media

print(total)

lst = [47, 11, 42, 13]

max_find = lambda a, b: a if (a > b) else b

max = reduce(max_find, lst)

print('max {}'.format(max))
