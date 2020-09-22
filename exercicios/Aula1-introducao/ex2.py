# TT007 - Introdução à Ciência de Dados

# Criado por: Matheus Percário Bruder

# Exercicio 02
# Escreva um programa que leia o valor do raio de um círculo e calcule o diâmetro e a área do círculo.
# (Considere π = 3.14159).

r = int(input('Raio: '))
print()


d = 2*r
print(f'Diametro: {d:.2f}', end=' | ')

a = 3.14159 * (r**2)
print(f'Area: {a:.2f}')
