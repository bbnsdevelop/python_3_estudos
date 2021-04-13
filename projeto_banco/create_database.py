#!/usr/bin/python3
# coding: utf-8

from config_conexao import get_conexao


def create_datadase():
    con = get_conexao()
    cursor = con.cursor()
    if cursor:
        cursor.execute("CREATE DATABASE IF NOT EXISTS agenda")
    else:
        print('Curso null')


if __name__ == '__main__':
    create_datadase()
