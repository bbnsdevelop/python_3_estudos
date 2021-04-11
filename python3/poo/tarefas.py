#!/usr/bin/python3
# coding: utf-8

from datetime import datetime, timedelta


class TarefaNaoEncontrada(Exception):
    pass

class Projeto:
    def __init__(self, nome):
        self.nome = nome
        self.tarefas = []

    def __iter__(self):
        return self.tarefas.__iter__()

    # sobrecarga de operador +=
    def __iadd__(self, tarefa):
        tarefa.dono = self
        self._add_tarefa(tarefa)
        return self

    def _add_tarefa(self, tarefa, **kwargs):
        self.tarefas.append(tarefa)

    def _add_nova_tarefa(self, descricao, **kwargs):
        self.tarefas.append(Tarefa(descricao, kwargs.get('vencimento', None)))

    def add(self, tarefa, vencimento=None, **kwargs):
        funcao_escolhida = self._add_tarefa if isinstance(tarefa, Tarefa) else self._add_nova_tarefa
        kwargs['vencimento'] = vencimento
        funcao_escolhida(tarefa, **kwargs)

    def tarefas_pendentes(self):
        return [tarefa_pendente for tarefa_pendente in self.tarefas if not tarefa_pendente.feito]

    def find_tarefa(self, decricao):
        try:
            return [tarefa for tarefa in self.tarefas if tarefa.descricao == decricao][0]
        except IndexError as e:
            raise TarefaNaoEncontrada(str(e))

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
        self.dono = None

    def concluir(self):
        super().concluir()
        novo_vencimento = datetime.now() + timedelta(days=self.dias, minutes=1)
        nova_tarefa =  TarefaRecorrente(self.descricao, novo_vencimento, self.dias)
        if self.dono:
            self.dono += nova_tarefa
        return nova_tarefa


def main():
    project = Projeto('Casa')
    project.tarefas.append(Tarefa('Lavar roupas'))
    project += TarefaRecorrente('Trocar lençóis', datetime.now(), 7)
    project.find_tarefa('Trocar lençóis').concluir()
    project.add('Lavar Pratos')
    project.add('Recolher o lixo', datetime.now())
    project.add('Lavaro banheiro', datetime.now() + timedelta(days=3, minutes=12))

    [tarefa.concluir() for tarefa in project.tarefas if tarefa.descricao == 'Lavar Pratos']

    try:
        project.find_tarefa('Trocar almofadas').concluir()
    except TarefaNaoEncontrada as e:
        print(f'Causa foi {str(e)}')

    print(project)
    tarefas_pendentes = []

    for tarefa in project.tarefas_pendentes():
        tarefas_pendentes.append(tarefa.descricao)

    print(f'Total de Tarefas - {project.tarefas.__len__()}')
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
