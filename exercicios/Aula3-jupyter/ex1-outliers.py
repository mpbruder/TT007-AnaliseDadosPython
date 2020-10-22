# TT007 - Introdução à Ciência de Dados

# Criado por: Matheus Percário Bruder

# Exercicio 01
"""
Ao analisar os dados coletados como parte de um experimento científico, pode ser desejável remover os valores mais extremos antes de realizar outros cálculos. 
Escreva uma função que recebe uma lista de valores e um inteiro não negativo, N, como seus parâmetros. A função deve criar uma nova cópia da lista com os N maiores elementos e o N menores elementos removidos. Em seguida, ele deve retornar a nova cópia da lista como o único resultado da função. A ordem dos elementos na lista retornada não precisa coincidir com a ordem dos elementos na lista original.
Escreva um programa principal que demonstre sua função. Sua função deve ler uma lista de números do usuário e remover os maiores e os menores valores a partir dele. Exibe a lista com os outliers removidos, seguido pela lista original.
"""

import random
import statistics as st

# -------------------------------------------------------------------
# FUNÇÕES
# -------------------------------------------------------------------


def gerador_lista(inicio, fim, tamanho):
    # sample retorna uma lista com números nao repetidos
    # range = população
    # tamanho = amostra
    lista = random.sample(range(inicio, fim + 1), tamanho)
    return lista


def func(lista, n):
    outliers = []
    m = st.mean(lista)
    for num in lista:
        if num < m - n or num > m + n:
            outliers.append(num)
    return outliers


# -------------------------------------------------------------------
# MAIN
# -------------------------------------------------------------------

l = gerador_lista(0, 100, 20)
print(f'Lista original: {l}')
print(f'Média: {st.mean(l)}')

while True:
    n = int(input('\nDigite um limite: '))
    if n > 0:
        break

o = func(l, n)
print(f'Outliers: {o}')