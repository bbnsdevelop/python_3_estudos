#!/usr/bin/python3
# coding: utf-8


def fatoral(n):
    return n * (fatoral(n -1) if (n - 1 ) > 1 else 1)


if __name__ == '__main__':
    print(f'10! = {fatoral(10)}')
