#!/usr/bin/python3
# coding: utf-8

from config_db import get_connection
from mysql.connector.errors import ProgrammingError
from Contatos import Contato


def select_contatos():
    contatos = []
    with get_connection() as connection:
        try:
            sql = 'SELECT id, nome, tel FROM contatos ORDER BY nome'
            cursor = connection.cursor()
            cursor.execute(sql)
            for response in cursor.fetchall():
                contatos.append(Contato(*response))
        except ProgrammingError as e:
            print(f'Erro ao buscar contatos {e.msg}')

    for contato in contatos:
        print(contato)


def select_contato_by_id(id):
    contato = None
    with get_connection() as connection:
        try:
            sql = 'SELECT id, nome, tel FROM contatos WHERE id = %s'
            # sql = 'SELECT id, nome, tel FROM contatos WHERE id = {}'.format(id) # pode causar um sql injection
            # cursor.execute(sql)

            cursor = connection.cursor()
            cursor.execute(sql, (id,))
            response = cursor.fetchone()
            contato = Contato(*response)
        except ProgrammingError as e:
            print(f'Erro ao buscar contato por id {e.msg}')

    print(contato)


def delete_contato_by_id(id):
    with get_connection() as connection:
        try:
            sql = 'DELETE FROM contatos WHERE id = %s'
            cursor = connection.cursor()
            cursor.execute(sql, (id, ))
            connection.commit()
        except ProgrammingError as e:
            print(f'Erro ao deletar contato por id {e.msg}')
        else:
            print(f'{cursor.rowcount} registro(s) deletad(s).')


def update_contato_by_id(contato):
    with get_connection() as connection:
        try:
            sql = 'UPDATE contatos SET nome = %s, tel = %s WHERE id = %s'
            cursor = connection.cursor()
            cursor.execute(sql, contato)
            connection.commit()
        except ProgrammingError as e:
            print(f'Erro ao atualizar contato por id {e.msg}')
        else:
            print(f'{cursor.rowcount} registro(s) atualidado(s).')


def select_contato_by_name(name):
    contatos = []
    with get_connection() as connection:
        try:
            sql = "SELECT id, nome, tel FROM contatos WHERE nome like %s "
            params = (f'%{name}%',)
            cursor = connection.cursor()
            cursor.execute(sql, params)
            for response in cursor.fetchall():
                contatos.append(Contato(*response))
        except ProgrammingError as e:
            print(f'Erro ao buscar contato por nome {e.msg}')
    for contato in contatos:
        print(contato)


if __name__ == '__main__':
    select_contatos()
    print('------------Buscando-pelo-id-4----------------')
    select_contato_by_id(4)
    # select_contato_by_id('4; drop table emails') # sql injection
    print('------------Buscando-pelo-nome----------------')
    select_contato_by_name('ca')
    delete_contato_by_id(8)
    contato_update = ('Mario Martins', '9822-8875', 5)
    update_contato_by_id(contato_update)
