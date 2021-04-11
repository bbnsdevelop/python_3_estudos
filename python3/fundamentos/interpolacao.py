#!/usr/bin/python
# coding: utf-8

from string import Template

nome, idade = 'Jose', 30

print('Nome: %s idade: %d' % (nome, idade))
print('Nome: {} idade: {}'.format(nome, idade))
print('Nome: {0} idade: {1}'.format(nome, idade))
print('Nome: {1} idade: {0}'.format(idade, nome))
print(f'Nome: {nome} Idade: {idade}')


s = Template('Nome: $nome Idade: $idade')
print(s.substitute(nome=nome, idade=idade))
