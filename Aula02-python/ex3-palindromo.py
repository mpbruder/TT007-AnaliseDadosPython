# TT007 - Introdução à Ciência de Dados

# Criado por: Matheus Percário Bruder

# Exercicio 03
"""
Uma palindrome é um número ou um texto cuja leitura é a mesma tanto de frente para traz como de traz para frente. Por exemplo, cada um dos seguintes números de 5 dígitos são palindromes: 12321, 55555, 45554 e 11611. Escreva um script que leia um número de N dígitos e determine se este é ou não uma palindrome. 

Não deve ser usado vetores (array).
"""


num = input('Numero: ')
tamanho = len(num)

if tamanho % 2 == 0:
    limite = tamanho / 2
else:
    limite = (tamanho - 1) / 2


# definindo tamanho de 'cortador' 
multi = '1'
for i in range(1, tamanho):
    multi += '0'
multi = int(multi)


for i in range(1, int(limite) + 1):
    num = int(num)

    primeiro = int((num // ((len(str(num)) * multi) / len(str(num)))))  # Pega primeiro
    num %= int((len(str(num)) * multi) / len(str(num)))  # Retira primeiro

    ultimo = num % 10  # Pega ultimo
    num //= 10  # Retira o quinto

    #print(f'numero == {num}')
    
    multi = int(multi / 100)

    if primeiro != ultimo:
        is_palindrome = False
    else:
        is_palindrome = True

        
if is_palindrome:
    print(f'SIM! É palindromo')
else:
    print(f'NÃO! Não são palindromos')

