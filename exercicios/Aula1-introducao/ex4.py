# TT007 - Introdução à Ciência de Dados

# Criado por: Matheus Percário Bruder

# Exercicio 04
"""
Um triângulo retangulo pode ter lados que são inteiros. O conjunto desses três valores é chamado tripla Pitagorea. Estes lados devem satisfazer a relação de que a soma dos quadrados dos lados é igual ao quadrado da hipotenusa.
Encontre todas as triplas Pitagoreas, cujos valores para os lados e para a hipotenusa sejam menores que 20.

Use um for triplo aninhado para tentar todas as possibilidades. Este método é chamado computação por força bruta. Para diversos problemas computacionais não existe outro algoritmo senão a força bruta!
"""

for a in range(1, 21, 1):
    for b in range(1, 21, 1):
        for c in range(1, 21, 1):
            if c**2 == a**2 + b**2:
                print(f'Tripla pitagorea: a ={a:3} | b ={b:3} | c ={c:3}')
