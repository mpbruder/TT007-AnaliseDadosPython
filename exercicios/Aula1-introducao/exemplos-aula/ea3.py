# TT007 - Introdução à Ciência de Dados

# Criado por: Matheus Percário Bruder

# Exemplo
"""
A maioria dos anos tem 365 dias. No entanto, o tempo necessário para a Terra orbitar o Sol é um pouco mais do que isso. Como resultado, um dia extra, 29 de fevereiro, está incluído em alguns anos para corrigir essa diferença. Esses anos são chamados de anos bissextos.

As regras para determinar se um ano é ou não um ano bissexto são as seguintes:
    • Qualquer ano divisível por 400 é um ano bissexto.
    • Dos anos restantes, qualquer ano divisível por 100 não é um ano bissexto.
    • Dos anos restantes, qualquer ano divisível por 4 é um ano bissexto.
    • Todos os outros anos não são anos bissextos.
    
Escreva um programa que leia um ano do usuário e exiba uma mensagem indicando seja ou não um ano bissexto.
"""

def bissexto(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False

y = input(f'Type a year: ').strip()
if y.isdigit():
    y = int(y)
    resp = bissexto(y)
    if resp:
        print(f'{y} is leap (bissexto)')
    else:
        print(f'{y} is not leap (bissexto)')
