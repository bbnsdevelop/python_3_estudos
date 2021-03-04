#!/usr/bin/python
# coding: utf-8

class Carro:
    def __init__(self, marca, cor, valor, modelo, qtd_portas):
        self.marca = marca
        self.cor = cor
        self.valor = valor
        self.modelo = modelo
        self.qtd_portas = qtd_portas

    def get_marca(self):
        return self.marca

    def set_marca(self, marca):
        self.marca = marca

    def get_cor(self):
        return self.cor

    def set_cor(self, cor):
        self.cor = cor

    def get_valor(self):
        return self.valor

    def set_valor(self, valor):
        self.valor = valor

    def get_modelo(self):
        return self.modelo

    def set_modelo(self, modelo):
        self.modelo = modelo

    def get_qtd_portas(self):
        return self.qtd_portas

    def set_qtd_portas(self, qtd_portas):
        self.qtd_portas = qtd_portas

    def exbir(self):
        print('--------------------------------------------------------------------')
        print('Dados do carro:')
        print('Marca: '+ self.marca +', modelo: ' + self.modelo + ', cor: ' + self.cor + ', valor: R$ ' + str(self.valor) + ', ' + str(self.qtd_portas) + ' portas')
