#!/usr/bin/python3
# coding: utf-8


def fibo(quantidade, sequencia=(0, 1)):
    return sequencia if quantidade == len(sequencia) \
        else fibo(quantidade, sequencia + (sum(sequencia[-2:]),))


if __name__ == '__main__':
    response = fibo(25)
    for num in response:
        print(f'{num}', end=',')

