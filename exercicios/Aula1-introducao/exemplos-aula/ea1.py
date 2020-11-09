# TT007 - Introdução à Ciência de Dados

# Criado por: Matheus Percário Bruder

# Exemplo
"""
Escreva um programa que leia um número inteiro positivo (n) do usuário e, em seguida, exiba a soma de todos os inteiros de 1 a n. A soma dos primeiros n inteiros positivos pode ser calculado usando a fórmula: sm = n(n+1)/2
"""

# Lendo inteiro do teclado
n = int(input('Numero: '))

# Computando a soma
sm = (n * (n + 1)) / 2

# Print do resultado
print(f'A soma dos números naturais 1 a {n} é: {int(sm)}')
