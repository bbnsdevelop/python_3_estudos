#!/usr/bin/python
# coding: utf-8


def escreva():
    try:
        file = open('testeFile.txt', 'r')
        file.write('Testandooo')
        print('Gravou com sucesso')
    except IOError as e:
        print('Erro ao escrever no arquivo', e)
    finally:
        print('Fechando arquivo')
        file.close()

escreva()
