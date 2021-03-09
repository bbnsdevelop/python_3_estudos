#!/usr/bin/python
# coding: utf-8

salary = 1550


def decorador(func):
    def funcao_interna():
        global salary
        if salary == 1500:
            salary = 1000
        func()  # aqui executa a função passada por parâmetro

    return funcao_interna


@decorador
def precisa_decorar():
    global salary
    if salary == 1600:
        salary = salary * 10 / 100 + salary
    else:
        salary = salary * 12 / 100 + salary

    print('new salary is: ${}'.format(salary))


@decorador
def calcular_novo_salario():
    global salary
    salary = 1500

    def novo():
        print('novo salario: {}'.format(salary))

    novo()


calc = calcular_novo_salario
calc()
precisa_decorar()
