#!/usr/bin/python3
# coding: utf-8


def fibo(quantidade, sequencia=(0, 1)):

    if quantidade == len(sequencia):
        return sequencia
    return fibo(quantidade, sequencia + (sum(sequencia[-2:]),))


if __name__ == '__main__':
    response = fibo(30)
    for num in response:
        print(f'{num}', end=',')

