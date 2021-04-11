#!/usr/bin/python3
# coding: utf-8

from mysql.connector import connect


conexao = connect(
    host='127.0.0.1',
    user='root',
    password='123asd'
)

print(conexao)
