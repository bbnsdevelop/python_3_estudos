#!/usr/bin/python
# coding: utf-8

import datetime


def getToday():
    return datetime.date.today()


def get_year_of_birth():
    year = int(input('Digite ano do nascimento: '))
    month = int(input('Digite mês do nascimento: '))
    day = int(input('Digite dia do nascimento: '))
    return datetime.date(year, month, day)


def main():
    print('Calculando sua idade')
    dias = getToday() - get_year_of_birth()
    print('você tem {} vividos'.format(dias))


main()
