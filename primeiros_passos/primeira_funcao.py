#!/usr/bin/python
# coding: utf-8


def main():
    print('Olá estou chamando uma função')

main()

def somaDoisNumeros(num1, num2):
    """
    soma dois números
    """
    print('a soma é: {}'.format(num1 + num2))

somaDoisNumeros(4, 6)

print('------------------------')

def primo(num):
    """
    metodo verifica se um número é primo
    """
    for n in range(2, num):
        if num % n == 0:
            print('Não é primo ' + str(num))
            break
        else:
            print('Primo ' + str(num))
            break


primo(8)
primo(9)
primo(115)
    