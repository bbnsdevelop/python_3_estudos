# coding=utf-8

# -*- coding: utf-8 -*-

meuNome = 'Bruno Batista'
print(meuNome)
print(len(meuNome))

#if (len(meuNome) == 13)
#    print('Entrou no if')

print(meuNome) # para o python uma str é um vetor

# indexação
print(meuNome[:]) # retorna toda a string
print(meuNome[0]) # pega primeira posição
print(meuNome[ 0:5 ]) # duas posições do array
print(meuNome[ :-1 ]) # retorna a primeira posição ate a -1 que eh letra 'a' final do vetor
print(meuNome[ ::2 ]) # espaçamento pega de dois em dois elementos do vetor
print(meuNome[ ::-1 ]) # inverte a str

# a posição do index de uma str é imutável
#meuNome[0] = "b" # erro--------> object does not support item assignment
print(meuNome + ' Ninguém')

letra = 'b'
print(letra * 4)

s = "Sammy"
print(s[2:])