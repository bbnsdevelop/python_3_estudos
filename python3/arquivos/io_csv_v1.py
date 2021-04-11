#!/usr/bin/python3
# coding: utf-8

import csv
from Pessoa import Pessoa


def read_file():
    peoples = []
    with open('pessoas.csv') as file:
        for pessoa in csv.reader(file):
            peoples.append(Pessoa(*pessoa))
    return peoples


if __name__ == '__main__':
    data = read_file()
    data.sort(key=lambda pessoa: pessoa.age)
    for pessoa in data:
        print('Nome: {}, Idade: {}'.format(pessoa.name, pessoa.age))
