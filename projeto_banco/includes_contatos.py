#!/usr/bin/python3
# coding: utf-8

from mysql.connector.errors import ProgrammingError
from config_db import get_connection


def include_contato():
    sql = 'INSERT INTO contatos (nome, tel) VALUES (%s, %s)'
    params = (
        ('Jose', '9877-7845'),
        ('Ana', '9877-9045'),
        ('Castilho', '9877-7775'),
        ('Mario', '9877-7215'),
        ('Ze', '9877-3545'),
        ('João', '9877-7455'),
        ('Bia', '9877-78574'),
        ('Carlos', '9877-45415'),
    )
    with get_connection() as connection:
        try:
            cursor = connection.cursor()
            cursor.executemany(sql, params)
            connection.commit()
        except ProgrammingError as e:
            print(f'Erro ao inserir contatos: {e.msg}')
        else:
            print(f'{cursor.rowcount} Registros incluidos')


if __name__ == '__main__':
    include_contato()