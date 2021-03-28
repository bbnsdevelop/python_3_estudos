#!/usr/bin/python3
# coding: utf-8

from datetime import datetime


class Projeto:
    def __init__(self, nome):
        self.nome = nome
        self.tarefas = []

    def __iter__(self):
        return self.tarefas.__iter__()

    def add(self, descricao):
        self.tarefas.append(Tarefa(descricao))

    def tarefas_pendentes(self):
        return [tarefa_pendente for tarefa_pendente in self.tarefas if not tarefa_pendente.feito]

    def find_tarefa(self, decricao):
        return [tarefa for tarefa in self.tarefas if tarefa.descricao == decricao][0]

    def __str__(self):
        return f'{self.nome} - {len(self.tarefas_pendentes())} tafera(s) pendente(s)'


class Tarefa:
    def __init__(self, descricao):
        self.descricao = descricao
        self.feito = False
        self.data_criacao = datetime.now()

    def concluir(self):
        self.feito = True

    def show_status(self):
        return self.descricao + ': (Conclída)' if self.feito else self.descricao + ': Aberta'

    def __str__(self):
        return self.descricao


def main():
    project = Projeto('Casa')
    project.tarefas.append(Tarefa('Lavar roupas'))
    project.add('Lavar Pratos')
    project.add('Recolher o lixo')
    project.add('Lavaro banheiro')

    [tarefa.concluir() for tarefa in project.tarefas if tarefa.descricao == 'Lavar Pratos']

    print(project)
    tarefas_pendentes = []

    for tarefa in project:
        tarefas_pendentes.append(tarefa.descricao)
    print(f'Tarefas pendentes - {tarefas_pendentes}')
    print(f'Tarefas conclídas - {project.find_tarefa("Lavar Pratos").descricao}')


if __name__ == '__main__':
    main()
