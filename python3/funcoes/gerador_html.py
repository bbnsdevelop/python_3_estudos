#!usr/bin/python3
# coding: utf-8


def tag_bloco(elemento, texto, classe='success'):
    return f'<{elemento} class="{classe}">{texto}</{elemento}>'


if __name__ == '__main__':
    # testes (assertions
    assert tag_bloco('div', 'Incluído com sucesso!') == \
        '<div class="success">Incluído com sucesso!</div>'
    print(tag_bloco('div', 'Incluído com sucesso!'))
