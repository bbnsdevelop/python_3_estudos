#!usr/bin/python3
# coding: utf-8

from random import randint


def jogar_um_numero():
    return randint(1, 6);


def exec():
    num = jogar_um_numero()
    for i in range(1, 7):
        if i % 2 == 1:
            continue
        if i == num:
            print("ACERTOU!!")
            break
    else:
        print('Infelizmente vc não acertou :(')


if __name__ == '__main__':
    exec()
