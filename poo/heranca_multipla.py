#!/usr/bin/python3
# coding: utf-8

class Animal:
    @property
    def capacidades(self):
        return ('Dormir', 'Comer', 'Beber')


class Homem(Animal):
    @property
    def capacidades(self):
        return super().capacidades + ('Fazer merda', 'Ser burro')


class Aranha(Animal):
    @property
    def capacidades(self):
        return super().capacidades + ('Soltar teia', 'Andar pela parede')


class SpiderMan(Homem, Aranha):
    @property
    def capacidades(self):
        return super().capacidades + ('Soltar teia entre predios', 'Ser medroso')


if __name__ == '__main__':
    peter = Homem()
    print(f'Suas capacidades: {peter.capacidades}')

    peter = SpiderMan()
    print(f'Suas capacidades: {peter.capacidades}')
