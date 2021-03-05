#!/usr/bin/python
# coding: utf-8

def decorador(func):
    def funcao_interna():
        print('codigo executado antes da função')
        func()
        print('Código executado depois da função')
    return funcao_interna

@decorador
def precisa_decorar():
    print('Essa função precisa de um decorador')


precisa_decorar()
