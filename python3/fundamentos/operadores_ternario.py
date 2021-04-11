#!/usr/bin/python
# coding: utf-8


def operador():
    esta_chuvendo = True
    estado_da_roupa = ('secas', 'molhadas')[esta_chuvendo]
    frase = 'Hoje estou com as roupas'
    formatacao = '{} {}'.format(frase, estado_da_roupa)
    print(formatacao)


operador()
