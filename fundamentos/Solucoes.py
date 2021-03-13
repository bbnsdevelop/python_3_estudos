#!/usr/bin/python
# coding: utf-8

st = 'Print only the words that start with s in this sentence'

split_string = st.split()

print('Palavras que começam com S')

for letra in split_string:
    if letra[0] == 's':
        print(letra)

print('números pares')

for rang in range(11):
    if rang % 2 == 0:
        print(rang)

print('compreesão de lista')

[ print(x) for x in range(1, 50) if x % 3 == 0 ]
