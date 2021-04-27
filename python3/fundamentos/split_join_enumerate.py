#!/usr/bin/python3
# coding: utf-8

frase = 'O Brasil é o país do futebol, o Brasil é penta.'


def split_string(param):
    global frase
    lista = frase.split(param)
    return lista





if __name__ == '__main__':
    print(split_string(' '))
    print(split_string(','))
    palavra = ''
    count = 0
    frase = split_string(' ')

    for valor in frase:
       qtd = frase.count(valor)

       if qtd > count:
           count = qtd
           palavra = valor

    print(f'Palavra que apareceu mais vezes é {palavra} qtd de vezes {count}')