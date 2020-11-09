# TT007 - Introdução à Ciência de Dados

# Criado por: Matheus Percário Bruder

# Exemplo
"""
Um número primo é um inteiro maior que 1 que só é divisível por um e por ele mesmo. 

Escreva uma função que determine se seu parâmetro é primo ou não, retornando Tre se for, e False caso contrário. Escreva um programa principal que leia um inteiro do usuário e exibe uma mensagem indicando se é primo ou não.
"""


def is_prime(number):
    for i in range(3, number, 2):
        if number % i == 0:
            return False
    return True


n = input('Type a number: ').strip()
if n.isdigit():
    n = int(n)
    resp = is_prime(n)
    if resp:
        print(f'{n} is prime')
    else:
        print(f'{n} is not prime')
