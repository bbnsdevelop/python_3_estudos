#!/usr/bin/python3
# coding: utf-8

def all_params(*args, **kwargs):
    print(f'args: {args}')
    print(f'kwargs: {kwargs}')


if __name__ == '__main__':
    all_params('a', 'b', 'c')
    all_params('a', 'b', 'c', legal=True, valor=12.18, name='Jose')
