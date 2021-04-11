#!/usr/bin/python
# coding: utf-8

from poo.book import Book

def inicializando_livro():
    book = Book('Três Marias','Luiz de Camom',100)
    book2 = Book('Java para leigos','Eu',1000)

    book.exiba_livro()
    book2.exiba_livro()

inicializando_livro()