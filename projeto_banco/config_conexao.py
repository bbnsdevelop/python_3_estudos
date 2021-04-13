#!/usr/bin/python3
# coding: utf-8

from mysql.connector import connect
import subprocess
count = 0


def get_conexao():
    global count
    if count == 0:
        try:
            conexao = connect(
                host='127.0.0.1',
                user='root',
                password='123asd'
            )
            return conexao
        except Exception as e:
            print('Erro ao conectar com o banco')
            count += 1
            get_conexao()
    elif count == 1:
        start_service_mysql_local()
        count = 0
        get_conexao()
    else:
        print('Erro ao conectar com o banco')


def start_service_mysql_local():
    subprocess.run(["systemctl", "start apache2"])
    subprocess.run(["service", "mysql start"])
