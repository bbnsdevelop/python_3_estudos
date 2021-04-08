#!/usr/bin/python3
# coding: utf-8

from locale import setlocale, LC_ALL
from calendar import mdays, month_name
from functools import reduce

# Brazil
setlocale(LC_ALL, 'pt_BR')

meses_31 = filter(lambda mes: mdays[mes] == 31, range(1, 13))
meses_nomes = map(lambda mes: month_name[mes], meses_31)
meses_string = reduce(lambda todos_meses, mes_nome: f'{todos_meses}\n - {mes_nome}', meses_nomes, 'Meses com 31 dias:')

print(meses_string)
