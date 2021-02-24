#!/usr/bin/python
# coding: utf-8

from Dog import Dog

def main():
    print('Criando um chachorro!!\n')
    viralata = Dog('Viralata caramelo')
    print(viralata.raca)
    viralata.latir()

    print('############################\n')

    trocaRaca(viralata)
    print('Transformação: ',viralata.raca)
    viralata.latir(lati='miauuuuuuuu2')

# referencia
def trocaRaca(dog):
    dog.raca = 'Pitibull 2'

main()