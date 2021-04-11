#!/usr/bin/python3
# coding: utf-8

def mutltiplicar(x):

    def calcular(y):
        return x * y
    return calcular


if __name__ == '__main__':
    dobro = mutltiplicar(2)
    triplo = mutltiplicar(3)

    print(f'o dobro de 3 é {dobro(3)}')
    print(f'o triplo é de 4 {triplo(4)}')

