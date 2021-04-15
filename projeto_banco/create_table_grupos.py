#!/usr/bin/python3
# coding: utf-8

from config_db import get_connection
from mysql.connector.errors import ProgrammingError


def create_table():
    table_grupos = """
        CREATE TABLE IF NOT EXISTS grupos(
            id INT AUTO_INCREMENT PRIMARY KEY,
            descricao VARCHAR(50)
        )
    """
    alter_contato_add_column = """
        ALTER TABLE contatos ADD COLUMN IF NOT EXISTS grupo_id INT
    """
    alter_contato = """        
        ALTER TABLE contatos ADD FOREIGN KEY IF NOT EXISTS (grupo_id) REFERENCES grupos(id)
    """

    with get_connection() as connection:
        try:
            cursor = connection.cursor()
            cursor.execute(table_grupos)
            cursor.execute(alter_contato_add_column)
            cursor.execute(alter_contato)
        except ProgrammingError as e:
            print(f'Erro ao executar script de DDL. Error:{e.msg}')


if __name__ == '__main__':
    create_table()
