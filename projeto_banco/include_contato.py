#!/usr/bin/python3
# coding: utf-8

from mysql.connector.errors import ProgrammingError
from config_db import get_connection


def include_contato():
    sql = 'INSERT INTO contatos (nome, tel) VALUES (%s, %s)'
    params = ('Tiaozinho', '98987-7845')
    with get_connection() as connection:
        try:
            cursor = connection.cursor()
            cursor.execute(sql, params)
            connection.commit()
        except ProgrammingError as e:
            print(f'Erro ao inserir contatos: {e.msg}')
        else:
            print(f'Registro incluido, ID: {cursor.lastrowid}')


if __name__ == '__main__':
    include_contato()