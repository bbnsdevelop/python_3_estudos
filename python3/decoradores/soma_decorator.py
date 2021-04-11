#!/usr/bin/python3
# coding: utf-8

def soma(a, b ):
    def soma_c(c):
        return a + b + c
    return soma_c


if __name__ == '__main__':
    soma_c = soma(3, 2)
    print(soma_c(5))

    print(soma(1, 4)(5))
