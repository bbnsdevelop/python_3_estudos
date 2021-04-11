#!/usr/bin/python
# coding: utf-8

def leiaUmNumero():
    contErro = 0
    continua = True
    listaDeNumero = []
    while continua:
        try:
            numero = int(input('Informe um numero: '))
            listaDeNumero.append(numero)
            resposta = input('Deseja continuar? Sim ou Nao ')
            if resposta.startswith('S'):
                continua = True
            else:
                continua = False
        except Exception as e:
            contErro += 1
            print('Erro ao adicionar numero na lista ', e)

    exibaInformacoes(contErro, listaDeNumero)


def exibaInformacoes(contErro, listaDeNumero):
    print('Quantidade de erros {}'.format(contErro))
    print('Números digitados foram {}'.format(listaDeNumero))


leiaUmNumero()
