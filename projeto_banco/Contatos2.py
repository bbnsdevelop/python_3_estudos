#!/usr/bin/python3
# coding: utf-8

class Contato:
    def __init__(self, id, nome, tel, grupo):
        self.nome = nome
        self.tel = tel
        self.id = id
        self.grupo = grupo

    def __str__(self):
        return f'Id: {str(self.id)} Nome: {self.nome}, Telefone: {self.tel} Grupo: {self.grupo}'
