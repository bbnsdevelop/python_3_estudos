#!/usr/bin/python3
# coding: utf-8

class Funcionario(object):
    def __init__(self):
        self.__salario = 1200
        self.__profissao = 'Ajudante Geral'
    
    def setSalario(self, sal):
        self.__salario = sal
    
    def getSalario(self):
        return self.__salario
    

    def setProfissao(self, profissao):
        self.__profissao = profissao
    
    def getProfissao(self):
        return self.__profissao

class Gerente(Funcionario):
    def __init__(self):
        super().setSalario(5000)
        super().setProfissao('Gerente de Estoque')


if __name__ == '__main__':
    g = Gerente()
    print(g.getProfissao())
    print(g.getSalario())

    f = Funcionario()
    print(f.getProfissao())
    print(f.getSalario())