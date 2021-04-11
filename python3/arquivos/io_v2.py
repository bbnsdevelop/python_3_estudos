#!/usr/bin/python3
# coding: utf-8

from Pessoa import Pessoa


def leitura2():
    peoples = []
    with open('pessoas.csv') as file:
        for people in file:
            peoples.append(Pessoa(*people.strip().split(',')))
    return peoples


def gravar(people):
    with open('pessoas.csv', 'w') as file:
        print('{},{}'.format(people.name, people.age), file=file)


def leitura():
    peoples = []
    try:
        file = open('pessoas.csv')
        # dessa forma o for faz algo parecido com stream lendo sob demanda o arquivo
        for people in file:
            peoples.append(Pessoa(*people.strip().split(',')))
    except IndexError as e:
        print('Error when was open file {}'.format(e))
    finally:
        file.close()
    return sorted(peoples, key=lambda pessoa: pessoa.age)


def showInfo(peoples):

    for p in peoples:
        p.show_people()


if __name__ == '__main__':
    data = leitura2()
    showInfo(data)
    # people = Pessoa('Araão', 19)
    # gravar(people)
    data = leitura()
    print('--------------------------------')
    showInfo(data)
