#!/usr/bin/python3
# coding: utf-8

class Carro:
    def __init__(self, velocidade_max):
        self.velocidade_atual = 0
        self.velocidade_max = velocidade_max

    def acelerar(self, aceleracao=5):
        if self.velocidade_atual >= self.velocidade_max:
            self.velocidade_atual = self.velocidade_max
        else:
            self.velocidade_atual += aceleracao
            if self.velocidade_atual > self.velocidade_max:
                self.velocidade_atual = self.velocidade_max

    def get_velocidade_atual(self):
        return self.velocidade_atual

    def frear(self, frenagem=5):
        if self.get_velocidade_atual() <= 0:
            self.velocidade_atual = 0
        else:
            self.velocidade_atual -= frenagem


def show_velocity(carro):
    print(f'Velocidade atual = {carro.get_velocidade_atual()}')


if __name__ == '__main__':
    c1 = Carro(180)
    for _ in range(25):
        c1.acelerar(aceleracao=8)
        show_velocity(c1)
    print('--------------------------------')

    for _ in range(10):
        c1.frear(frenagem=20)
        show_velocity(c1)
