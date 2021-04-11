#!/usr/bin/python3
# coding: utf-8

from functools import reduce
import nomes_filter as filtro


def sum_age(pessoas):
    init_age = 0
    return reduce(lambda age, p: age + p['idade'], pessoas, init_age)


if __name__ == '__main__':
    pessoas = [
        {'nome': 'Pedro', 'idade': 18},
        {'nome': 'Ana', 'idade': 20},
        {'nome': 'Henrique', 'idade': 17},
        {'nome': 'Marcio', 'idade': 19},
        {'nome': 'Juriscreuza', 'idade': 10},
        {'nome': 'Rafael', 'idade': 8},
    ]

    print(f'total de idades: {sum_age(pessoas)}')
    menores = filtro.filtro_menores(pessoas)
    print(f'soma de idade pessoas menores de idade {sum_age(menores)}')
    pessoas_nomes_maiores_de_5 = filtro.filtro_nomes_com_maisde5_caracteres(pessoas)
    print(f'soma de idade pessoas com nomes grandes {sum_age(pessoas_nomes_maiores_de_5)}')
