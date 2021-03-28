#!/usr/bin/python3
# coding: utf-8

from pacotes.p1 import modulo_soma


def log(func):
    def decorator(*args, **kwargs):
        print(f'Inicio da chamada da funcção: {func.__name__}')
        print(f'agrs: {args}')
        print(f'kwargs: {kwargs}')
        resultado = func(*args, **kwargs)
        print(f'Resultado da chamada: {resultado}')
        return resultado
    return decorator


@log
def soma(x, y):
    return modulo_soma.soma(x, y)


@log
def sub(x, y):
    return x - y


if __name__ == '__main__':
    soma(4, 6)
    sub(8, 3)
