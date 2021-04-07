#!/usr/bin/python3
# coding: utf-8


def filtro_menores(list_pessoas):
    pessoas = filter(lambda menor: menor['idade'] < 18, list_pessoas)
    return pessoas


def filtro_nomes_com_maisde5_caracteres(list_pessoas):
    pessoas = filter(lambda pessoa: pessoa['nome'].__len__() > 5, list_pessoas)
    return pessoas


if __name__ == '__main__':
    pessoas = [
        {'nome': 'Pedro', 'idade': 18},
        {'nome': 'Ana', 'idade': 20},
        {'nome': 'Henrique', 'idade': 17},
        {'nome': 'Marcio', 'idade': 19},
        {'nome': 'Juriscreuza', 'idade': 10},
        {'nome': 'Rafael', 'idade': 8},
    ]
    print(list(filtro_menores(pessoas)))
    print(list(filtro_nomes_com_maisde5_caracteres(pessoas)))
