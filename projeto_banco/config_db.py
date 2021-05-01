#!/usr/bin/python3
# coding: utf-8

from mysql.connector import connect
from contextlib import contextmanager


@contextmanager
def get_connection():
    connection = connect(**get_config())
    try:
        yield connection
    finally:
        if connection and connection.is_connected():
            connection.close()


def get_config():
    configs = []
    with open('config_db.csv') as file:
        for conf in file:
            for index in conf.strip().split(','):
                configs.append(index)

    params = dict(
        host=configs[0],
        port=configs[1],
        user=configs[2],
        password=configs[3],
        database=configs[4]
    )
    return params
