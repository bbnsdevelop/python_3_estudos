#!/usr/bin/python3
# coding: utf-8

from config_db import get_connection
from mysql.connector.errors import ProgrammingError


def create_table():
    table_contatos = """
        CREATE TABLE IF NOT EXISTS contatos(
            nome VARCHAR(50), tel VARCHAR(40)
        )
    """
    table_emails = """
        CREATE TABLE IF NOT EXISTS emails(
            id INT AUTO_INCREMENT PRIMARY KEY,
            dono VARCHAR(50)
        )
    """

    with get_connection() as connection:
        try:
            cursor = connection.cursor()
            cursor.execute(table_contatos)
            cursor.execute(table_emails)
        except ProgrammingError as e:
            print(f'Erro ao executar script de DDL. Error:{e.msg}')


def drop_email():
    query = """
        DROP TABLE IF EXISTS emails
    """
    with get_connection() as connection:
        try:
            cursor = connection.cursor()
            cursor.execute(query)
        except ProgrammingError as e:
            print(f'Erro ao executar script DROP - DDL. Error:{e.msg}')


def show_tables():
    query = """
        SHOW TABLES
    """
    tables = []
    with get_connection() as connection:
        try:
            cursor = connection.cursor()
            cursor.execute(query)
            for table in enumerate(cursor):
                tables.append(table[1])
        except ProgrammingError as e:
            print(f'Erro ao executar script DROP - DDL. Error:{e.msg}')

    print(tables)


if __name__ == '__main__':
    create_table()
    show_tables()
