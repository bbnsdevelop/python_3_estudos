#!/usr/bin/python
# coding: utf-8


def menu():
    continuar=1
    while continuar:
        continuar = int(input("0. Sair \n"+
                              "1. Iniciar o Jogo\n"))
        if continuar:
            game()
        else:
            print("Saindo...")

def game():
    jogada=0

    while ganhou() == 0:
        print("\nJogador ", jogada%2 + 1)
        exibe()
        linha = 0
        coluna = 0
        try:
            linha  = int(input("\nLinha :"))
            coluna = int(input("Coluna:"))        
        except Exception as e:
            print('Por favor digitar apenas números!')
            game()
            
        if linha > board.__len__() or coluna > board.__len__():
            print('Não existe essa lina ou coluna no tabuleiro!')
            game()
        else:
            if board[linha-1][coluna-1] == 0:
                if(jogada%2+1)==1:
                    board[linha-1][coluna-1]=1
                else:
                    board[linha-1][coluna-1]=-1
            else:
                print("Nao esta vazio")
                jogada -=1

            if ganhou():
                print("Jogador ",jogada%2 + 1," ganhou apos ", jogada+1," rodadas")

            jogada +=1
    
def ganhou():
    #checando linhas
    for i in range(3):
        soma = board[i][0]+board[i][1]+board[i][2]
        if soma==3 or soma ==-3:
            return 1

     #checando colunas
    for i in range(3):
        soma = board[0][i]+board[1][i]+board[2][i]
        if soma==3 or soma ==-3:
            return 1

    #checando diagonais
    diagonal1 = board[0][0]+board[1][1]+board[2][2]
    diagonal2 = board[0][2]+board[1][1]+board[2][0]
    if diagonal1==3 or diagonal1==-3 or diagonal2==3 or diagonal2==-3:
        return 1

    return 0

def exibe():
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                print(" _ ", end =' ')
            elif board[i][j] == 1:
                print(" X ", end =' ')
            elif board[i][j] == -1:
                print(" O ", end =' ')

        print()
                

board= [ [0,0,0],
         [0,0,0],
         [0,0,0] ]

menu()