#!/usr/bin/python3
# coding: utf-8

from config_db import get_connection
from mysql.connector.errors import ProgrammingError
from Contatos2 import Contato


def select_contatos():
    contatos = []
    with get_connection() as connection:
        try:
            sql = 'SELECT c.id, c.nome, c.tel, g.descricao FROM contatos c ' \
                  'INNER JOIN grupos g on c.grupo_id = g.id ORDER BY nome'
            cursor = connection.cursor()
            cursor.execute(sql)
            for response in cursor.fetchall():
                contatos.append(Contato(*response))
        except ProgrammingError as e:
            print(f'Erro ao buscar contatos {e.msg}')

    for contato in contatos:
        print(contato)


if __name__ == '__main__':
    select_contatos()
