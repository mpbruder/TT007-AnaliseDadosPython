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
    system('cls')
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
    time.sleep(1)


def inicio_jogo():
    system('cls')
    while True:
        np = int(input('Quantos jogadores?\n: '))
        if np < 2 or np > 5:
            print("Escolha entre 2 e 5 jogadores.")
            pause()
            system('cls')
        else:
            break
    return np


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


def rolar_dados(inf_player):
    inf_player[2] = [0, 0, 0, 0, 0]

    # Adicionar somente numero correto de dados
    for d in range(inf_player[1]):
        inf_player[2][d] = random.randrange(1, 7)

    return inf_player


def iniciar_npc(n_players):
    cpu_players = []
    for i in range(n_players):
        # pegar nome aleatório da lista de nomes
        name = NAMES[random.randint(0, len(NAMES)-1)]
        NAMES.remove(name)  # retirar nome escolhido da lista
        player = [name, 5, list()]
        cpu_players.append(player)
    return cpu_players


def mostrar_dados(dice):
    string = ''
    for d in dice:
        if d == 0:
            continue
        string += f'[{d}] '
    return string


def validar_aposta(old_bet, new_bet):
    if old_bet[0] > new_bet[0] or (old_bet[0] == new_bet[0] and old_bet[1] >= new_bet[1]) or new_bet[0] > 24 or new_bet[1] > 6:
        return False
    else:
        return True


def contar_dados(p, valor):
    total = 0
    for x in range(num_players):
        d = p[x][2].count(valor)
        total += d
        print(f'{p[x][0]} possui {d} ({valor}): {mostrar_dados(p[x][2])}')

    print(f'Existe um total de {total} ({valor}) na mesa.\n')
    pause()
    return total


def dados_em_jogo(inf_players):
    t = 0
    for p in inf_players:
        t += p[1]
    return t


def aposta(who, p, p_name, old_bet):
    new_bet = [0, 0]
    if p[who][0] == p_name:
        while True:
            new_bet = input(
                'Faça sua aposta! [Número de dados] [Valor do dado]\n: ')
            new_bet = new_bet.split()
            if len(new_bet) > 1 and new_bet[0].isdigit() and new_bet[1].isdigit():
                new_bet = [int(new_bet[0]), int(new_bet[1])]
                if validar_aposta(old_bet, new_bet):
                    break
    else:
        total_dados = dados_em_jogo(p)
        while True:
            b1 = random.randrange(total_dados)
            b2 = random.randrange(1, 7)
            new_bet = [int(b1), int(b2)]
            if validar_aposta(old_bet, new_bet):
                break
    print(p[who][0] + ' apostou que existem ' + str(new_bet[0]) +
          ' dados com valor [' + str(new_bet[1]) + '] na mesa.\n')
    pause()
    return new_bet


def escolha_humana():
    print(
        'Você gostaria de [a]postar, chamar o jogador anterior de [m]entiroso, ou [c]oncordar com o palpite do jogador anterior?')
    while True:
        res = input(': ')
        if res == 'a':
            return 0
        if res == 'm':
            return 1
        if res == 'c':
            return 2
        print('Escolha inválida. Escolha entre as letras: a, m, ou c.')


def escolha_npc():
    r = random.randrange(0, 3)
    if r == 0:
        return 0
    elif r == 1:
        return 1
    elif r == 2:
        return 2
    pass


def mentiroso(who, p, old_bet):
    print(f'\n{p[who][0]} acha que o jogador anterior está mentindo.\n')
    if contar_dados(p, old_bet[1]) >= old_bet[0]:
        p[who][1] -= 1
        print(
            f'Errado! {p[who][0]} perdeu um dado, agora possui apenas {p[who][1]}.')
    else:
        p[(who-1) % num_players][1] -= 1
        print(f'Boa, {p[who][0]}! O jogador anterior perdeu um dado.')
    return p


def concordar(who, p, old_bet):
    print(f'{p[who][0]} acha que o jogador anterior está falando a verdade.\n')
    if contar_dados(p, old_bet[1]) == old_bet[0]:
        print(f'Boa, {p[who][0]}! Todo mundo perdeu um dado.\n')
        for x in range(num_players):
            if x != who:
                p[x][1] -= 1
                print(f'{p[x][2]} tem agora apenas {p[x][1]} dados.')
    else:
        p[who][1] -= 1
        print(
            f'Errado! {p[who][0]} perdeu um dado, agora possui apenas {p[who][1]}.')
    pause()
    return p


def remover_player(inf_players):
    max_players = num_players
    losers = []
    for p in range(num_players):
        if inf_players[p][1] == 0:
            max_players -= 1
            print(inf_players[p][0] + ' está fora do jogo.\n')
            pause()
            losers.append(x)
    return [inf_players, max_players]


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
players.append([player_name, 5, list()])
system('cls')  # limpar tela

gameContinues = True
nextPlayer = random.randrange(num_players - 1)  # definir quem começa

# Inicio de jogo
while gameContinues:
    # definir dados da rodada
    for x in range(num_players):
        players[x] = rolar_dados(players[x])

    aposta_atual = [0, 6]
    if players[nextPlayer][0] == player_name:
        print(f'\nSua mão: {mostrar_dados(players[nextPlayer][2])}')
        print(f'Existem {str(contar_dados(players))} outros dados na mesa.')
    print(
        f'{players[nextPlayer][0]} começa. Por favor, faça a primeira aposta.\n')
    aposta_atual = aposta(nextPlayer, players, player_name, aposta_atual)

    # Continuando os rounds
    status = True
    while status:
        nextPlayer = (nextPlayer + 1) % (num_players)

        # Mostrando opções ao jogador
        if players[nextPlayer][0] == player_name:
            print(
                f"É sua vez. Sua mão: {mostrar_dados(players[nextPlayer][2])}")
            print(
                f'Existem outros {str(dados_em_jogo(players) - players[nextPlayer][1])} dados na mesa.')
            escolha = escolha_humana()
        else:
            escolha = escolha_npc()

        # Determinando escolhas
        if escolha == 0:
            aposta_atual = aposta(nextPlayer, players,
                                  player_name, aposta_atual)
        elif escolha == 1:
            players = mentiroso(nextPlayer, players, aposta_atual)
            status = False
        elif escolha == 2:
            players = concordar(nextPlayer, players, aposta_atual)
            status = False

    # Remover jogador da partida
    rm = remover_player(players)
    players = rm[0]
    if num_players != rm[1]:
        num_players = rm[1]
        nextPlayer = (nextPlayer-1) % num_players
    rm = []

    if num_players == 1:
        status = False
        print(f'\n\nPARABÉNS! {players[nextPlayer][0]} ganhou o jogo.')
