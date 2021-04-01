#!/usr/bin/python3
# coding: utf-8


class RGB:
    def __init__(self):
        self.cores = ['red', 'green', 'blue'][::-1]

    def __iter__(self):
        return self

    def __next__(self):
        try:
            return self.cores.pop()
        except IndexError:
            raise StopIteration()


if __name__ == '__main__':
    colors = RGB()
    print(next(colors))
    print(next(colors))
    print(next(colors))

    try:
        print(next(colors))
        print(next(colors))
    except StopIteration:
       print('Acabou')

    for cor in RGB():
        print(cor)
