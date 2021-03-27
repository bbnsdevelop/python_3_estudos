#!usr/bin/python3
# coding: utf-8


def tag_bloco(conteudo, *args, classe='success', inline=False):
    tag = 'span' if inline else 'div'
    html = conteudo if not callable(conteudo) else conteudo(*args)
    return f'<{tag} class="{classe}">{html}</{tag}>'


def tag_lista(*itens):
    lista = ''.join((f'<li>{item}</li>' for item in itens))
    return f'<ul>{lista}</ul>'


if __name__ == '__main__':
    print(tag_bloco('Incluído com sucesso!'))
    print(tag_bloco('Incluído com sucesso2!', inline=True))
    print(tag_bloco(inline=True, conteudo='Incluído com sucesso3!'))
    print(tag_bloco(inline=True, conteudo='Incluído com sucesso4!', classe='row'))

    lista = ['Jose', 'Maria', 'João']

    print(tag_lista(lista[0], lista[1], lista[2]))

    print(tag_bloco(conteudo=tag_lista(*lista), classe='row'))

    print(tag_bloco(tag_lista, 'Sabado','Domingo', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', classe='row'))
