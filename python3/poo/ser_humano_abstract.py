#!/usr/bin/python3
# coding: utf-8

from abc import ABCMeta, abstractproperty

class Humano(metaclass=ABCMeta):
    especie = 'Homo Sapiens'

    def __init__(self, nome):
        self.nome = nome
        self._idade = None

    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, idade):
        if idade < 0:
            raise ValueError('Idade deve ser um número positivo!')
        else:
            self._idade = idade

    @property
    @abstractproperty
    def inteligente(self):
        pass

    def das_cavernas(self):
        self.especie = 'Homo Neanderthalensis'
        return self

    @staticmethod
    def especies():
        adijetivos = ('Habils', 'Erectus', 'Neanderthalensis', 'Sapiens')
        return ('Australopiteco',) + tuple(f'Homo{adj}' for adj in adijetivos)

    @classmethod
    def is_evoluido(cls):
        return cls.especie == cls.especies()[-1]

    @classmethod
    def origem_evolucao(cls):
        return [especie for especie in cls.especies() if cls.especie == especie]


class Neanderthal(Humano):
    especie = Humano.especies()[-2]

    @property
    def inteligente(self):
        return False


class HomoSapiens(Humano):
    especie = Humano.especies()[-1]

    @property
    def inteligente(self):
        return True


if __name__ == '__main__':
    jose = HomoSapiens('Jośe')
    grug = Neanderthal('Grug').das_cavernas()

    jose.idade = 30

    print(f'tipo humano {Humano.especie}')
    print(f'tipo humano das cavernas: {grug.especie}')
    print(f'tipo humano {jose.especie}')
    print(f'Nome: {jose.nome} - Idade: {jose.idade}')

    joao = HomoSapiens('João')
    ugga = Neanderthal('Ugga')
    print(f'Evolução (a partir da classe): {", ".join(HomoSapiens.especies())}')
    print(f'{joao.nome} Evolução (a partir da classe): {", ".join(joao.especies())}')
    print(f'{ugga.nome} Evolução (a partir da classe): {", ".join(ugga.especies())}')
    print(f'{joao.nome} É evoluído? {"Sim" if joao.is_evoluido() else "Não"}')
    print(f'{ugga.nome} É evoluído? {"Sim" if ugga.is_evoluido() else "Não"}')
    ugga.idade = 400
    print(f'{joao.nome} É evoluído? {"Sim" if joao.is_evoluido() else "Não"} Origem da evolução: \
            {joao.origem_evolucao()[0]} É inteligente? {joao.inteligente}')
    print(f'{ugga.nome} É evoluído? {"Sim" if ugga.is_evoluido() else "Não"} Origem da evolução: \
            {ugga.origem_evolucao()[0]} - Idade: {ugga.idade} É inteligente? {ugga.inteligente}')
