#!/usr/bin/python3
# coding: utf-8


def comprehension_generator():
    generator = (r ** 2 for r in range(10) if r % 2 == 0)

    for ge in generator:
        print('Pares {}'.format(ge))


if __name__ == '__main__':
    comprehension_generator()
