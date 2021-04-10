#!/usr/bin/python3
# coding: utf-8


def mdc(numeros):
    def calc(dividor):
        return dividor if sum(map(lambda x: x % dividor, numeros)) == 0 else calc(dividor - 1)
    return calc(min(numeros))


if __name__ == '__main__':
    print(mdc([21, 7]))
    print(mdc([124, 40]))
    print(mdc([9, 564, 66, 3]))
    print(mdc([55, 22]))
    print(mdc([15, 150]))
    print(mdc([7, 9]))
