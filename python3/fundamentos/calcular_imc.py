#!/usr/bin/python3
# coding: utf-8

def get_peso_altura():
    altura = float(input("Digite sua altura: "))
    peso = float(input("Digite sua peso: "))
    return (altura, peso)


def imc(altura, peso):
    return peso / (altura**2)


if __name__ == '__main__':
    dados = get_peso_altura()
    imc = imc(*dados)
    print(f'Seu IMC é {imc:.2F}')
    if imc < 18.5:
        print("Abaixo do peso")
    elif 18.5 < imc < 24.9:
        print('Nomal')
    elif 25 < imc < 29.9:
        print('Sobrepeso')
    elif 30 < imc < 34.9:
        print('Obesidade fase 1')
    elif 35 < imc < 39.9:
        print('Obesidade fase 2')
    else:
        print('Obesidade fase 3')
