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
import time

from os import system
from sys import exit

NAMES = 'Amanda Fernando Giovana Lucca Vitória Matheus Gustavo Maria José Geraldo Stella Nicolli Gabriel Pedro Tadeu'.split()

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


def pause():
    time.sleep(2)


def inicio_jogo():
    system('cls')
    while True:
        p = int(input('Quantos jogadores?\n: '))
        if p < 2 or p > 5:
            print("Escolha entre 2 e 5 jogadores.")
            pause()
            system('cls')
        else:
            break
    return p


def menu(*args):
    for key, value in enumerate(args):
        print(f'{key} - {value}')

    while True:
        opc = int(input(': '))
        if opc < 0 or opc > (len(args) - 1):
            print("Opção inválida!")
        elif opc == 0:
            exit()
        else:
            break
    return opc


def rolar_dados(playerInfo):
    d1 = random.randrange(1, 7)
    d2 = random.randrange(1, 7)
    d3 = random.randrange(1, 7)
    d4 = random.randrange(1, 7)
    d5 = random.randrange(1, 7)
    playerInfo[1] = [d1, d2, d3, d4, d5]
    return playerInfo


def iniciar_npc(n_players):
    cpu_players = []
    for i in range(n_players):
        # pegar nome aleatório da lista de nomes
        name = NAMES[random.randint(0, len(NAMES)-1)]
        NAMES.remove(name)  # retirar nome escolhido da lista
        player = [name, list()]
        cpu_players.append(player)
    return cpu_players


def mostrar_dados(dice):
    d1, d2, d3, d4, d5 = dice
    return f'[{d1}], [{d2}], [{d3}], [{d4}], [{d5}]'


def validar_aposta(oldBet, newBet):
    if oldBet[0] > newBet[0] or (oldBet[0] == newBet[0] and oldBet[1] >= newBet[1]) or newBet[0] > 24 or newBet[1] > 6:
        return False
    else:
        return True


def contar_dados(tot_players):
    dados = 0
    for p in tot_players:
        dados = dados + len(p[1])
    # print(f'total dados {dados}')
    return dados


def aposta(who, p, p_name, oldBet):
    newbet = [0, 0]
    if p[who][0] == p_name:
        while True:
            newbet = input('Faça sua aposta! [Número de dados] [Valor do dado]')
            newbet = newbet.split()
            if len(newbet) > 1 and newbet[0].isdigit() and newbet[1].isdigit():
                newbet = [int(newbet[0]), int(newbet[1])]
                if validar_aposta(oldBet, newbet):
                    break
    else:
        total_dados = contar_dados(p)
        while True:
            b1 = random.randrange(total_dados)
            b2 = random.randrange(1, 7)
            newbet = [int(b1), int(b2)]
            if validar_aposta(oldBet, newbet):
                break
    print(p[who][0] + ' apostou que existem ' + str(newbet[0]) + ' dados com valor [' + str(newbet[1]) + '] na mesa.\n')
    pause()
    return newbet


def escolha_humana():
    print('Você gostaria de [a]postar, chamar o jogador anterior de [m]entiroso, ou [c]oncordar com o palpite do jogador anterior?')
    while True:
        res = input(': ')
        if res == 'a':
            return 0
        if res == 'm':
            return 1
        if res == 'c':
            return 2
        print('Escolha inválida. Escolha entre as letras: a, m, ou c.')


# Programa principal ====================================================
# =======================================================================
game_tile()
opc = menu('Sair', 'Iniciar')
system('cls')  # limpar tela

# definindo opções de jogo
player_name = input('Qual é seu nome?\n: ').strip().capitalize()
if player_name in NAMES:
    NAMES.remove(player_name)
num_players = inicio_jogo()
players = iniciar_npc(num_players - 1)
players.append([player_name, list()])


# Inicio de jogo
system('cls')  # limpar tela
gameContinues = True
nextPlayer = random.randrange(0, num_players - 1)  # definir quem começa


while gameContinues:
    # definir dados da rodada
    for x in range(num_players):
        players[x] = rolar_dados(players[x])

    roundContinues = True
    currentBet = [0, 6]
    if players[nextPlayer][0] == player_name:
        print(f'\nSua mão: ({mostrar_dados(players[nextPlayer][1])})')
        print('Existem ' + str(contar_dados(players)) + ' outros dados na mesa.')
    print(players[nextPlayer][0] + ' começa. Por favor, faça a primeira aposta.\n')
    currentBet = aposta(nextPlayer, players, player_name, currentBet)
    while roundContinues:
        nextPlayer = (nextPlayer+1) % (num_players)
        if players[nextPlayer][0] == player_name:
            print(f"É sua vez. Sua mão: ({mostrar_dados(players[nextPlayer][1])})")
            print('Existem ' + str(contar_dados(players)) + ' outros dados na mesa.')
            escolha = escolha_humana()

    print(currentBet)
    break

print(players)
