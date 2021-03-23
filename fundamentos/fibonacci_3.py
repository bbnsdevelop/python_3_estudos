#!/usr/bin/python3
# coding: utf-8


def fibo(quantidade):
    resultado = [0, 1]

    while True:
        resultado.append(sum(resultado[-2:]))
        if quantidade == len(resultado):
            break

    return resultado


if __name__ == '__main__':
    response = fibo(30)
    for num in response:
        print(f'{num}', end=',')

