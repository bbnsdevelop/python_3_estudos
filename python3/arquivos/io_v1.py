#!/usr/bin/python3
# coding: utf-8

from Pessoa import Pessoa


def leitura():
    file = open('pessoas.csv')
    data = file.read()
    file.close()
    return data


def showInfo(data):
    peoples = []
    for people in data.splitlines():
        peoples.append(Pessoa(*people.split(',')))

    for p in peoples:
        p.show_people()


if __name__ == '__main__':
    data = leitura()
    showInfo(data)
