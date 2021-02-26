#!/usr/bin/python
# coding: utf-8

class Book(object):
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def exiba_livro(self):
        print('Você está lendo o livro:')
        print('Nome: {}'.format(self.titulo))
        print('Autor: {}'.format(self.autor))
        print('paginas: {}'.format(self.paginas))
        if self.paginas > 100:
            print('Este livro possui mais de 100 paginas')
        else:
            print('Livro tem menos de 100 paginas')
