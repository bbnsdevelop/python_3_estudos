#!/usr/bin/python3
# coding: utf-8


def faixa_etaria(idade):
    try:
        if 0 <= idade < 18:
            return 'Menor de idade'
        elif idade in range(18, 64):
            return 'Adulto'
        elif idade in range(65, 100):
            return 'Melhor idade'
        elif idade >= 100:
            return 'Matuzalem'
        else:
            return 'Idade inválida'
    except Exception as e:
        return 'Idade inválida'



if __name__ == '__main__':
    for idade in (17, 35, 87, 113, -4, 1000, 'a'):
        print(f'{idade}: {faixa_etaria(idade)}')
