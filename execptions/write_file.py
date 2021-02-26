#!/usr/bin/python
# coding: utf-8


def escreva():
    try:
        file = open('testeFile.txt', 'w')
        file.write('Testandooo')
    except IOError:
        file.close()

escreva()
