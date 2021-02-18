#!/usr/bin/python
# -*- coding: utf-8 -*-

listaNotas = [10,10,8,6]


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



# tupas

tuplas = (1,2,3,4,5,6)

for tupla in tuplas:
    print('números: ', tupla)

tuplasDeLista = [(12, 2), (3,5), (7, 9)]

for (t1, t2) in tuplasDeLista:
    print('mutiplicação de {} com {} é igual {}'.format(t1, t2, (t1 * t2 )))