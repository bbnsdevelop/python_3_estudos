#!/usr/bin/python3
# coding: utf-8


def dobro(x):
    return x * 2


def quadrado(x):
    return x ** 2


if __name__ == '__main__':
    funcs = [dobro, quadrado] * 5
    for func, num in zip(funcs, range(1, 11)):
        print(f'função {func.__name__} de {num} = {func(num)}')

    d = dobro
    print(d(5))

    q = quadrado
    print(q(5))
