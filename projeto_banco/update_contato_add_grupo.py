#!/usr/bin/python3
# coding: utf-8

from mysql.connector.errors import ProgrammingError
from config_db import get_connection


def update_contatos(data):
    with get_connection() as connection:
        sql = 'UPDATE contatos SET grupo_id= %s WHERE id = %s'
        try:
            cursor = connection.cursor()
            cursor.execute(sql, data)
            connection.commit()
        except ProgrammingError as e:
            print(f'Erro ao fazer updade do contato {e.msg}')
        else:
            print(f'{cursor.rowcount} Registro(s) atualizado(s)')


if __name__ == '__main__':
    data = (1, 1)
    update_contatos(data)
    data = (2, 7)
    update_contatos(data)
    data = (3, 5)
    update_contatos(data)
    data = (1, 6)
    update_contatos(data)
    data = (2, 9)
    update_contatos(data)
    data = (3, 3)
    update_contatos(data)
