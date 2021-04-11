#!usr/bin/python
# coding: utf-8


def calc_preco_final(preco_bruto, calc_imposto, **params):
    return preco_bruto + preco_bruto * calc_imposto(**params)


def calc_imposto_importado(is_importado):
    return 0.22 if is_importado else 0.13


def cal_imposto_explosivo(is_explosivo, fator_mult=1):
    return 0.11 * fator_mult if is_explosivo else 0


if __name__ == '__main__':
    preco_bruto = 134.98
    preco_final = calc_preco_final(preco_bruto, calc_imposto_importado, is_importado=True)
    preco_final = calc_preco_final(preco_final, cal_imposto_explosivo, is_explosivo=True, fator_mult=1.5)
    print(f'Preço final do produto calculado os impostos é R${preco_final}')
