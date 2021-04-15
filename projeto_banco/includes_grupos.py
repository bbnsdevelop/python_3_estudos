#!/usr/bin/python3
# coding: utf-8

from mysql.connector.errors import ProgrammingError
from config_db import get_connection


def include_grupos():
    sql = 'INSERT INTO grupos (descricao) VALUES (%s)'
    params = (
        ('Trabalho',),
        ('Inglês', ),
        ('Python',)
    )
    with get_connection() as connection:
        try:
            cursor = connection.cursor()
            cursor.executemany(sql, params)
            connection.commit()
        except ProgrammingError as e:
            print(f'Erro ao inserir grupos: {e.msg}')
        else:
            print(f'{cursor.rowcount} Registros incluidos')


if __name__ == '__main__':
    include_grupos()
