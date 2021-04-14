#!/usr/bin/python3
# coding: utf-8

class Contato:
    def __init__(self, id, nome, tel):
        self.nome = nome
        self.tel = tel
        self.id = id

    def __str__(self):
        return f'Id: {str(self.id)} Nome: {self.nome}, Telefone: {self.tel}'
