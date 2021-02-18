#!/usr/bin/python
# -*- coding: utf-8 -*-

listaNotas = []

for nota in range(4):
    listaNotas.append(float(input('Digite a nota {}: '.format( nota + 1))))


somaDasNotas = 0
media = 0
for notas in listaNotas:
    somaDasNotas +=notas

media = somaDasNotas / listaNotas.__len__()

if media == 10.0:
    print('Aluno excelente tirou média: ', str(media))
elif media > 7 and media <= 10:
    print('Aluno regular tirou média: ', str(media))
elif media < 7 and media > 5:
    print('Aluno reprovado tirou média: ', str(media))
elif media <= 5 and media > 0:
    print('Aluno ruim tirou média: ', str(media))
else:
    print('Não existe média abaixo de zero ou acima de: ', str(media))



