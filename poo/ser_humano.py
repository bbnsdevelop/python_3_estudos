#!/usr/bin/python3
# coding: utf-8

class Humano:
    especie = 'Homo Sapiens'

    def __init__(self, nome):
        self.nome = nome

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
        return [ especie for especie in cls.especies() if cls.especie == especie]


class Neanderthal(Humano):
    especie = Humano.especies()[-2]


class HomoSapiens(Humano):
    especie = Humano.especies()[-1]


if __name__ == '__main__':
    jose = Humano('Jośe')
    grug = Humano('Grug').das_cavernas()

    print(f'tipo humano {Humano.especie}')
    print(f'tipo humano das cavernas: {grug.especie}')
    print(f'tipo humano {jose.especie}')

    joao = HomoSapiens('João')
    ugga = Neanderthal('Ugga')
    print(f'Evolução (a partir da classe): {", ".join(HomoSapiens.especies())}')
    print(f'{joao.nome} Evolução (a partir da classe): {", ".join(joao.especies())}')
    print(f'{ugga.nome} Evolução (a partir da classe): {", ".join(ugga.especies())}')
    print(f'{joao.nome} É evoluído? {"Sim" if joao.is_evoluido() else "Não"}')
    print(f'{ugga.nome} É evoluído? {"Sim" if ugga.is_evoluido() else "Não"}')

    print(f'{joao.nome} É evoluído? {"Sim" if joao.is_evoluido() else "Não"} Origem da evolução: {joao.origem_evolucao()[0]}')
    print(f'{ugga.nome} É evoluído? {"Sim" if ugga.is_evoluido() else "Não"} Origem da evolução: {ugga.origem_evolucao()[0]}')
