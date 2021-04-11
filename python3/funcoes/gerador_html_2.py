#!usr/bin/python3
# coding: utf-8


def tag_bloco(elemento, texto, classe='success', inline=False):
    if inline:
        elemento = 'span'
    return f'<{elemento} class="{classe}">{texto}</{elemento}>'


if __name__ == '__main__':
    print(tag_bloco('div', 'Incluído com sucesso!'))
    print(tag_bloco('div', 'Incluído com sucesso2!', inline=True))
    print(tag_bloco('div', inline=True, texto='Incluído com sucesso3!'))
    print(tag_bloco('div', inline=True, texto='Incluído com sucesso4!', classe='row'))
