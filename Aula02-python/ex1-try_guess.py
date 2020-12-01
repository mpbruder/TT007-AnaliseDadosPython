# TT007 - Introdução à Ciência de Dados

# Autor: Matheus Percário Bruder

# Exercicio 01 - Adivinhe um número
"""
Escreva um programa que seleciona um número entre 1 e 1000 para ser adivinhado.

"""

import random


def sort_number():
    """Função gera um número aleatório entre 1 e 1000.

    Returns:
        int: número aleatório entre 1 e 1000.
    """
    return random.randrange(1, 1001)


sorted_num = sort_number()  # número sorteado
player_num = int(input('Número: '))  # numero do jogador


while sorted_num != player_num:
    diference = sorted_num - player_num  # diferença entre numeros

    # Teste
    # print(f'escolhido {sorted_num} \ndiferença {sorted_num - player_num}')

    if 1000 > diference >= 500:
        print(f'Muito pequeno, tente novamente!')
    elif 500 > diference >= 50:
        print(f'Pequeno, tente aumentar um pouco mais!')
    elif 50 > diference >= 10:
        print(f'Passou perto, mas ainda pequeno!')
    elif 10 > diference >= -10:
        print(f'Muito perto...')
    elif -10 > diference >= -50:
        print(f'Passou perto, mas ainda grande!')
    elif -50 > diference >= -500:
        print(f'Grande, tente diminuir um pouco!')
    elif -500 > diference >= -1000:
        print(f'Muito grande, tente novamente!')

    player_num = int(input('Número: '))  # outra escolha

print(f'Congratulations! The number was \'{sorted_num}\'.')
