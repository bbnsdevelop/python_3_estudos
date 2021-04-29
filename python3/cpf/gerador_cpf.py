#!/usr/bin/python3
# coding: utf-8

from random import randint
import validacpf as validator


def gerar_numeros_aleatorios():
    return str(randint(100000000, 999999999))


def cpf_sem_digito():
    return gerar_numeros_aleatorios()


def gerar_cpf():
    novo_cpf = cpf_sem_digito()
    reverso = 10
    total = 0
    for index in range(19):
        if index > 8:
            index -= 9
        total += int(novo_cpf[index]) * reverso
        reverso -= 1
        if reverso < 2:
            reverso = 11
            digito = 11 - (total % 11)
            if digito > 9:
                digito = 0
            total = 0
            novo_cpf += str(digito)
    return novo_cpf


if __name__ == '__main__':
    cpf_aleatorio = gerar_cpf()
    print(f'cpf: {cpf_aleatorio}')
    validator.validar_cpf(cpf_aleatorio)
