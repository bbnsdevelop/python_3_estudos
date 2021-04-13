#!/usr/bin/python3
# coding: utf-8

from config_db import get_connection

with get_connection() as connection:
    if connection.is_connected():
        print('Conectado')
