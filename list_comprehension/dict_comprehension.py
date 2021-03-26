#!/usr/bin/python3
# coding: utf-8


def dict_comprehension():
    dict = {i: r * 2 for i, r in enumerate(range(0, 10)) if r % 2 == 0}

    print(dict)


if __name__ == '__main__':
    dict_comprehension()
