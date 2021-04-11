def exec(func):
    if callable(func):
        func()


def bom_dia():
    print('bom dia')


def boa_tarde():
    print('Boa tarde')


def boa_noite():
    print('Boa noite')


if __name__ == '__main__':
    exec(bom_dia)
    exec(boa_tarde)
    exec(boa_noite)
