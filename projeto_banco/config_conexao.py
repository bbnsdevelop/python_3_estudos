#!/usr/bin/python3
# coding: utf-8

from mysql.connector import connect


def get_conexao():
    try:
        conexao = connect(
            host='127.0.0.1',
            user='root',
            password='123asd'
        )
        return conexao
    except Exception as e:
            print('Erro ao conectar com o banco')
