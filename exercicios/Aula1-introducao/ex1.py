# TT007 - Introdução à Ciência de Dados

# Criado por: Matheus Percário Bruder

# Exercício 01 
# Escreva um programa que leia dois inteiros e determine se o primeiro é multiplo do segundo.

a = int(input('Primeiro numero: '))
b = int(input('Segundo numero: '))

if a % b == 0:
    print(f'SIM! {a} é multiplo de {b}')
else:
    print(f'NÃO são multiplos!')