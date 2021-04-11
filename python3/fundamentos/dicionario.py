#!/usr/bin/python
# coding: utf-8


dicionario = {'chave1': 'valor', 'chave2': 3}

print(dicionario)

for item in dicionario:
    print(dicionario[item])


lista = dicionario.values()

print(lista)


lista = dicionario.keys()

print(lista)
for i in lista:
    print(i)


pessoa = {'nome': 'Ana', 'idade': 38, 'cursos': ['Português', 'Inglês']}

print('Professora: {}'.format(pessoa['nome']))
print('Da aulas de:')
for curso in pessoa['cursos']:
    print(curso)

pessoa.update({'sexo': 'F'})
pessoa['cursos'].append('Alemão')
pessoa['cursos'].sort()

pessoa.update({'salario': 1200.00})

print(pessoa)

salario = pessoa.pop('salario')
print(salario)
print(pessoa)
