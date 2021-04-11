#!usr/bin/python3
# coding: utf-8


def tag_bloco(elemento, texto, classe='success', inline=False):
    if inline:
        elemento = 'span'
    return f'<{elemento} class="{classe}">{texto}</{elemento}>'


def tag_lista(*itens):
    lista = ''.join((f'<li>{item}</li>' for item in itens))
    return f'<ul>{lista}</ul>'


if __name__ == '__main__':
    print(tag_bloco('div', 'Incluído com sucesso!'))
    print(tag_bloco('div', 'Incluído com sucesso2!', inline=True))
    print(tag_bloco('div', inline=True, texto='Incluído com sucesso3!'))
    print(tag_bloco('div', inline=True, texto='Incluído com sucesso4!', classe='row'))

    lista = ['Jose', 'Maria', 'João']

    print(tag_lista(lista[0], lista[1], lista[2]))

    print(tag_bloco(elemento='div', texto=tag_lista(*lista), classe='info'))
