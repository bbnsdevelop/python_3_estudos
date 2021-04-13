#!/usr/bin/python3
# coding: utf-8

from config_conexao import get_conexao


def list_datadase():
    con = get_conexao()
    cursor = con.cursor()
    cursor.execute('SHOW DATABASES')

    for index, database in enumerate(cursor, start=1):
        print(f'Banco de dados {index}: {database[0]}')


if __name__ == '__main__':
    list_datadase()
