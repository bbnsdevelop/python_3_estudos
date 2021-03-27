#!usr/bin/python3
# coding: utf-8

filtro_bloco = ('bloco_accessKy', 'bloco_id')
filtro_ul = ('ul_id', 'ul_style')


def get_atrs(informados, suportado):
    return ' '.join(f'{k.split("_")[-1]}="{v}"' for k, v in informados.items() if k in suportado)


def tag_bloco(conteudo, *args, classe='success', inline=False, **novos_atrs):
    tag = 'span' if inline else 'div'
    html = conteudo if not callable(conteudo) else conteudo(*args, **novos_atrs)
    atributos = get_atrs(novos_atrs, filtro_bloco)
    return f'<{tag} {atributos} class="{classe}">{html}</{tag}>'


def tag_lista(*itens, **novos_atrs):
    lista = ''.join((f'<li>{item}</li>' for item in itens))
    return f'<ul {get_atrs(novos_atrs, filtro_ul)}>{lista}</ul>'


if __name__ == '__main__':
    print(tag_bloco('Incluído com sucesso!'))
    print(tag_bloco('Incluído com sucesso2!', inline=True))
    print(tag_bloco(inline=True, conteudo='Incluído com sucesso3!'))
    print(tag_bloco(inline=True, conteudo='Incluído com sucesso4!', classe='row'))

    lista = ['Jose', 'Maria', 'João']

    print(tag_lista(lista[0], lista[1], lista[2]))

    print(tag_bloco(conteudo=tag_lista(*lista), classe='row'))

    print(tag_bloco(tag_lista, 'Sabado', 'Domingo', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', classe='row'))

    print(tag_bloco(tag_lista, 'Item 1', 'Item 2', classe='info', bloco_accessKy='m', bloco_id='conteudo',\
                    ul_id='lista', ul_style='color: red'))
