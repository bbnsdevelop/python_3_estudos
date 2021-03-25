#!/usr/bin/python3
# coding: utf-8

import os.path
from urllib import request
import csv


def download_file(url, name, type_file):
    if os.path.isfile('{}.{}'.format(name, type_file)):
        print('Já foi feito o download!!!')
    else:
        with request.urlopen(url) as entrada:
            print('Iniciando download!!!')
            dados = entrada.read().decode('latin1')
            print('Download finalizado!!!')
            for cidade in csv.reader(dados.splitlines()):
                print(f'{cidade[8]}: {cidade[3]}')


if __name__ == '__main__':
    url, tipo, name = (r'http://files.cod3r.com.br/curso-python/desafio-ibge.csv','csv','desafio-ibge')
    download_file(url, name, tipo)
