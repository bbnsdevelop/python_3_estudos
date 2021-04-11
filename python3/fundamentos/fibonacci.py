#!/usr/bin/python3
# coding: utf-8


def fibo():
    penultimo = 0
    ultimo = 1
    print(f'{penultimo},{ultimo}', end=',')
    proximo = 0
    while proximo < 2000:
        proximo = penultimo + ultimo
        print(proximo, end=',')
        penultimo = ultimo
        ultimo = proximo


if __name__ == '__main__':
    fibo()

