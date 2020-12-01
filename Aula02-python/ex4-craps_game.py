# TT007 - Introdução à Ciência de Dados

# Autor: Matheus Percário Bruder

# ----------------------------------------------------------------------------
# CRAPS GAME
# ----------------------------------------------------------------------------

# Descrição
"""
O jogador lança dois dados. Então soma-se as faces dos dados:
    * Se a soma for 7 ou 11 na primeira rodada, o jogador ganha.
    * Se for 2, 3 ou 12 na primeira rodada ( ou CRAPS) o jogador perde.
    * Se a soma for 4, 5, 6, 8, 9 ou 10 na primeira rodada. Então esta soma se torna o ponto do jogador.
        * Para ganhar, o jogador continua jogando o dado até a soma ser igual a seu ponto. 
        * O jogador perde se a soma for igual a 7.
"""

import random


def roll_dice():
    """Função que rola dois dados.

    Returns:
        tuple: retorno é uma tupla com o resultado empacotado.
    """
    die1 = random.randrange(1, 7)
    die2 = random.randrange(1, 7)
    return (die1, die2)


def display_dice(dice):
    """Exibe na tela os dados e a respectiva soma.

    Args:
        dice (tuple): Uma tupla com valor de cada dado sorteado.
    """
    die1, die2 = dice
    print(f'Result: {die1} + {die2} = {sum(dice)}')


die_values = roll_dice()  # primeira rodada
display_dice(die_values)

sum_dies = sum(die_values)

if sum_dies in (7, 11):  # condição de vitória
    game_status = 'WON'
elif sum_dies in (2, 3, 12):  # condição de derrota
    game_status = 'LOSE'
else:  # segue o jogo
    game_status = 'CONTINUE'
    player_point = sum_dies
    print(f'My point is {player_point}')

# looping até chegar condição de vitoria ou derrota
while game_status == 'CONTINUE':
    die_values = roll_dice()  # outras rodadas
    display_dice(die_values)
    sum_dies = sum(die_values)

    if sum_dies == player_point:
        game_status = 'WON'
    elif sum_dies == 7:
        game_status = 'LOSE'

# Mensagem de vitória ou derrota
if game_status == 'WON':
    print(f'Congratulations, you WIN!')
else:
    print(f'You LOSE, try again!')
