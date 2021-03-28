#!/usr/bin/python3
# coding: utf-8

from datetime import datetime, timedelta


class Projeto:
    def __init__(self, nome):
        self.nome = nome
        self.tarefas = []

    def __iter__(self):
        return self.tarefas.__iter__()

    def add(self, descricao, vencimento=None):
        self.tarefas.append(Tarefa(descricao, vencimento))

    def tarefas_pendentes(self):
        return [tarefa_pendente for tarefa_pendente in self.tarefas if not tarefa_pendente.feito]

    def find_tarefa(self, decricao):
        return [tarefa for tarefa in self.tarefas if tarefa.descricao == decricao][0]

    def __str__(self):
        return f'{self.nome} - {len(self.tarefas_pendentes())} tafera(s) pendente(s)'


class Tarefa:
    def __init__(self, descricao, vencimento=None):
        self.descricao = descricao
        self.feito = False
        self.data_criacao = datetime.now()
        self.vencimento = vencimento

    def concluir(self):
        self.feito = True

    def add_vencimento(self, dias, minutos=0):
        self.vencimento = datetime.now() + timedelta(days=dias, minutes=minutos)

    def show_status(self):
        status = []
        if self.feito:
            status.append('Concluída')
        elif self.vencimento:
            if datetime.now() > self.vencimento:
                status.append('Vencida')
            else:
                dias = (self.vencimento - datetime.now()).days
                status.append(f'Venci em {dias} dias')
        else:
            status.append('A fazer')

        return f'{self.descricao}: ' + ' '.join(status)

    def __str__(self):
        return self.descricao


class TarefaRecorrente(Tarefa):
    def __init__(self, descricao, vencimento, dias=7):
        super().__init__(descricao, vencimento)
        self.dias = dias

    def concluir(self):
        super().concluir()
        novo_vencimento = datetime.now() + timedelta(days=self.dias, minutes=1)
        return TarefaRecorrente(self.descricao, novo_vencimento, self.dias)


def main():
    project = Projeto('Casa')
    project.tarefas.append(Tarefa('Lavar roupas'))
    project.tarefas.append(TarefaRecorrente('Trocar lençóis', datetime.now(), 7))
    project.tarefas.append(project.find_tarefa('Trocar lençóis').concluir())
    project.add('Lavar Pratos')
    project.add('Recolher o lixo', datetime.now())
    project.add('Lavaro banheiro', datetime.now() + timedelta(days=3, minutes=12))

    [tarefa.concluir() for tarefa in project.tarefas if tarefa.descricao == 'Lavar Pratos']

    print(project)
    tarefas_pendentes = []

    for tarefa in project.tarefas_pendentes():
        tarefas_pendentes.append(tarefa.descricao)

    print(f'Total de Tarefas - {len(project.tarefas)}')
    print(f'Tarefas pendentes - {tarefas_pendentes}')
    print(f'Tarefas conclídas - {project.find_tarefa("Lavar Pratos").descricao}')

    print('----------------------------------------------------')

    for tarefa in project:
        print(f' - {tarefa.show_status()}')
    print('----------------------------------------------------')

    for tarefa in project:
        if tarefa.descricao == 'Lavar roupas':
            tarefa.add_vencimento(2, 30)
        print(f' - {tarefa.show_status()}')


if __name__ == '__main__':
    main()
