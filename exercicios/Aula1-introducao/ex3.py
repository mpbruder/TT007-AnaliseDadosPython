# TT007 - Introdução à Ciência de Dados

# Criado por: Matheus Percário Bruder

# Exercicio 03
"""
Uma palindrome é um número ou um texto cuja leitura é a mesma tanto de frente para traz como de traz para frente. Por exemplo, cada um dos seguintes números de 5 dígitos são palindromes: 12321, 55555, 45554 e 11611. Escreva um script que leia um número de 5 dígitos e determine se este é ou não uma palindrome. 
Se o número não for de 5 dígitos, mostre um alerta ao usuário indicando o problema e permita que o usuário entre com um número correto após a emissão do alerta. Não deve ser usado vetores (array).
"""

while True:
    num = input('Numero: ')
    # print(type(num))
    reverso = ''

    if len(num) != 5:
        print(f'Tente novamente, o numero \'{num}\' não possui 5 digitos!')
        continue
    else:
        for i in num[::-1]:
            reverso += i
        if reverso != num:
            print(f'NÃO! {num} e {reverso} não são palindromos')
            break
        else:
            print(f'SIM! {num} e {reverso} são palindromos')
            break
        
        
