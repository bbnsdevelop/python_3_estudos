#!/usr/bin/python3
# coding: utf-8

class Humano:
    especie = 'Homo Sapiens'

    def __init__(self, nome):
        self.nome = nome

    def das_cavernas(self):
        self.especie = 'Homo Neanderthalensis'
        return self


if __name__ == '__main__':
    jose = Humano('Jośe')
    greeg = Humano('Greeg').das_cavernas()

    print(f'tipo humano {Humano.especie}')
    print(f'tipo humano das cavernas: {greeg.especie}')
    print(f'tipo humano {jose.especie}')