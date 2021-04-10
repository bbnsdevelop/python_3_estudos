#!/usr/bin/python3
# coding: utf-8


def cores_arco_iris():
    yield 'Vermelho'
    yield 'Laranja'
    yield 'Amarelo'
    yield 'Verde'
    yield 'Verde'
    yield 'Azul'
    yield 'Índigo'
    yield 'Violeta'


if __name__ == '__main__':
    cores = cores_arco_iris()
    print(type(cores))
    while True:
        try:
            print(next(cores))
        except StopIteration as e:
            break

    print('---------FIM--WHILE-------')
    cores = cores_arco_iris()  # precisa ser atribuido novamente pois o while leu todos os dados
    for cor in cores:
        print(cor)
    else:
        print('---------FIM- FOR-------')
