#!/usr/bin/python3
# coding: utf-8


def resultado_f1(**podium):
    for index, piloto in podium.items():
        print(f'{index} -> {piloto}')


if __name__ == '__main__':
    resultado_f1(primeiro='Jose', segundo='Maira', terceiro='Marcio')
