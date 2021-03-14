#!/usr/bin/python
# coding: utf-8

lista = [1, 2, 3, 'João', 'Jonatas', 'Maria']
contem_na_lista = 'Jonatas' not in lista
print(contem_na_lista)

contem_na_lista = 'Jonatas' in lista
print(contem_na_lista)

lista = []

print('Tamando da lista: {}'.format(len(lista)))
lista.append(1)
lista.append(2)
lista.append('João')
lista.append('Zé')

print('Tamando da lista: {}'.format(len(lista)))

print(lista)
lista2 = ['nomes', 'telefone']

lista.append(lista2)
print(lista)
print(type(lista))

for l in lista:
    if isinstance(l, list):
        print('removido a lista: {} dentro da lista'.format(l))
        lista.remove(l)

print(lista)


nova_lista = ['Bruno', 'Tacy', 'João', 'Maria']

for index, nome in enumerate(nova_lista):
    if nome == 'João':
        del nova_lista[index]

print(nova_lista)
