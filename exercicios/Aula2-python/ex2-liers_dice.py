# TT007 - Introdução à Ciência de Dados

# Autor: Matheus Percário Bruder

# ----------------------------------------------------------------------------
# LIERS' DICE
# ----------------------------------------------------------------------------

# Descrição
"""
No Liers' dice, cada jogador recebe 5 dados. Em cada rodada os jogadores lançam os seus dados, mantendo suas faces escondidas dos demais jogadores. Cada jogador então escolhe uma face (1 a 6) e da um palpite de quantas faces iguais a esta há na mesa.

O próximo a jogar tem três alternativas:

    1. escolhe uma face e da um palpite, que deve ser necessariamente maior que o palpite anterior e passa para o próximo jogador

    2. chama o jogador anterior de mentiroso, neste caso abrem-se os dados e verifica-se o palpite corrente é verdadeiro. Se for o jogador atual perde um dado, senão o jogador anterior perde um dado.

    3. concorda com o palpite do jogador anterior. Neste caso, abrem-se os dados e se o palpite estiver correto, o jogador anterior perde dois dados.

Ganha o último jogador com dados na mesa.


Fonte: https://pt.wikipedia.org/wiki/Liar%27s_Dice_(jogo)#:~:text=Cada%20jogador%20recebe%20um%20copo,uma%20determinada%20face%20na%20mesa.
"""

import random

from os import system
from sys import exit

# Funções ===============================================================
# =======================================================================


def game_tile():
    print("""
            ##
            ##      __       _______    __       ____    _____  
            ##     / /|     /__  __/|  /  |     / _  \  /  __/|
            ##    / / /     |_/ /|_|/ /   |    / /_| |  \ \__|/ 
            ##   / / /       / / /   / /| |   / _   /|   \ \     
            ##  / /_/_   __ / /_/   / __  |  / / | |/ __ / /|   
            ## /_____/| /_______/| /_/|_|_| /_/ /|_| /____/ /   
            ## |_____|/ |_______|/ |_|/ |_| |_|/ |_| |____|/    
            ## 
            ##      ____      _______    _____    ______
            ##     / _  \    /__  __/|  / ___/|  / ____/|
            ##    / / | |    |_/ /|_|/ / /|__|/ / /___ |/
            ##   / / / /|     / / /   / / /    / ____/|
            ##  / /_/ / / __ / /_/   / /_/_   / /____|/
            ## /_____/ / /_______/|  |____/| /______/|
            ## |_____|/  |_______|/  |____|/ |______|/
            ##
            ## ---
    """)


def menu(*args):
    cont = 0
    for value in args:
        cont += 1
        print(f'{value} ', end='')
        if cont % 2 == 0:
            print()
        pass
    opc = int(input(': '))
    return opc


def jogar_dados():
    d1 = random.randrange(1, 7)
    d2 = random.randrange(1, 7)
    d3 = random.randrange(1, 7)
    d4 = random.randrange(1, 7)
    d5 = random.randrange(1, 7)
    return (d1, d2, d3, d4, d5)


def mostrar_dados(dice):
    d1, d2, d3, d4, d5 = dice
    return print(f'{d1}, {d2}, {d3}, {d4}, {d5}')


# Programa principal ====================================================
# =======================================================================
game_tile()
opc = menu('0', 'Sair', '1', 'Iniciar')
if opc == 0:
    exit()

system('cls')  # limpar tela

print('Escolha quantidade de jogadores')
n_players = menu('2','Dois', '3','Três', '4','Quatro', '5','Cinco')

players = []
for i in range(1, n_players):
    player = {}
    player['jogador'] = i
    player['dados'] = jogar_dados()
    players.append(player)

print(players)
