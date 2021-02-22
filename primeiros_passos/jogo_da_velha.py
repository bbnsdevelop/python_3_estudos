#!/usr/bin/python
# coding: utf-8

import random

from IPython.display import clear_output

def display_board(board):
    """
    Mostra o Tabuleiros
    """
    clear_output()
    print('\n')
    print ('\t  '+ board[7] + '  |  ' + board[8] + '  |  ' + board[9])
    
    print('\t-----------------')    
    print ('\t  '+ board[4] + '  |  ' + board[5] + '  |  ' + board[6])
    
    print('\t-----------------')    
    print ('\t  '+ board[1] + '  |  ' + board[2] + '  |  ' + board[3])
    print('\n')

def player_input():
    """
    Escolher X ou O
    """
    marker = ''
    while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1: Você quer ser X ou O ? ').upper()
    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')

def place_marker(board, marker, position):
    """
    Seta X ou O na posição escolhida
    """
    board[position] = marker

def win_check(board, marker):
    """
    Verifica se alguém venceu
    """
    place_maker = ((board[7] == marker and board[8] == marker and board[9] == marker) or
        (board[4] == marker and board[5] == marker and board[6] == marker) or
        (board[1] == marker and board[2] == marker and board[3] == marker) or
        (board[7] == marker and board[4] == marker and board[1] == marker) or
        (board[8] == marker and board[5] == marker and board[2] == marker) or
        (board[9] == marker and board[6] == marker and board[3] == marker) or
        (board[7] == marker and board[5] == marker and board[3] == marker) or
        (board[9] == marker and board[5] == marker and board[1] == marker))
    print('Testando place marker {} '.format(place_maker))
    return place_maker

def chooseFirst():
    """
    Escolhe quem começa de maneira randômica
    """
    if random.randint(0,1) == 0:
        return 'Player 1'
    else:
        return 'Player 2'

def spaceCheck(board, position):
    """
    Verifica se estar vazio
    """
    return board[position] == ' '

def fullBoardCheck(board):
    """
    Verifica as 10 posições se estão vazias
    """
    for index in range(0,10):
        if spaceCheck(board, index):
            return False

    return True

def player_choice(board):
    """
    Escolher uma posição de 1 a 9
    """
    position = ' '
    posicoes_tabuleiro = '1 2 3 4 5 6 7 8 9'.split()
    while position not in posicoes_tabuleiro or spaceCheck(board, int(position)):
        position = str(input('Escolha sua jogada (1-9): '))
        break
    return int(position)

def replay():
    """
    Continuar jogando
    """
    return input('Quer jogar novamente? "SIM" ou "NAO" ').lower().startswith('s')


def play():
    """
    Start o jogo
    """
    print("""
    Bem vindo ao jogo da velha
    versão: 1.0
    Data de criação: 18/02/2021
    """)
    while True:
            
        board = [' '] * 10
        marcador1, marcador2 = player_input()
        player = chooseFirst()

        print('Jogada do jogador: {}'.format(player))

        game_on = True

        while game_on:
            if player == 'Player 1':
                display_board(board)
                position = player_choice(board)
                place_marker(board, marcador1, position)
            if win_check(board, marcador1):
                display_board(board)
                print('Parabéns você venceu {}'.format(player))
                game_on = False
            else:
                if fullBoardCheck(board):
                    display_board(board)
                    print('Houve um empate entre os jogadores!')
                    break
                else:
                    player = 'Player 2'
            
            if player == 'Player 2':
                display_board(board)
                position = player_choice(board)
                place_marker(board, marcador2, position)
            if win_check(board, marcador2):
                display_board(board)
                print('Parabéns você venceu {}'.format(player))
                game_on = False
            else:
                if fullBoardCheck(board):
                    display_board(board)
                    print('Houve um empate entre os jogadores!')
                    break
                else:
                    player = 'Player 1'

        if not replay():
            break
        
play()