# TT007 - Introdução à Ciência de Dados

# Criado por: Matheus Percário Bruder

# Exemplo
"""
Crie um programa que leia três inteiros do usuário e os exiba de forma ordenada (do menor ao maior). Use as funções mínimo e máximo para encontrar o menor e maiores valores. O valor médio pode ser encontrado calculando a soma de todos os três valores e, em seguida, subtraindo o valor mínimo e o valor máximo.
"""

n1 = int(input(f'First number: ').strip())
n2 = int(input(f'Second number: ').strip())
n3 = int(input(f'Third number: ').strip())

maxi = max(n1, n2, n3)
mini = min(n1, n2, n3)

med = sum((n1, n2, n3)) - (maxi + mini)

print(f'\n{mini} -> {med} -> {maxi}')