# TT007 - Introdução à Ciência de Dados

# Criado por: Matheus Percário Bruder

# Exemplo
"""
Este exercício examina o processo de identificação do valor máximo em uma coleção de inteiros. Cada um dos inteiros será selecionado aleatoriamente a partir dos números entre 1 e 100. A coleção de inteiros pode conter valores duplicados, e alguns dos números inteiros entre 1 e 100 podem não estar presentes.

Pare um momento e pense em como você lidaria com esse problema no papel. Muitas pessoas verificariam cada inteiro em sequência e se perguntariam se o número que eles estão considerando atualmente é maior do que o maior número que eles viram anteriormente. Se for, então eles esquecem o número máximo anterior e lembram o número atual como o novo número máximo. Esta é uma abordagem razoável, e resultará na resposta correta quando o processo for executado com cuidado. Se vocês estivessem executando esta tarefa, quantas vezes você esperaria precisar atualizar o valor máximo e lembra de um novo número?

Embora possamos responder à pergunta feita no final do parágrafo anterior usando teoria da probabilidade, vamos explorá-la simulando a situação. Crie um programa que começa selecionando um número inteiro aleatório entre 1 e 100. Salve este inteiro como o número máximo encontrado até agora. Depois que o inteiro inicial foi selecionado, gera 99 inteiros aleatórios adicionais entre 1 e 100. Verifique cada inteiro conforme é gerado para ver se é maior do que o número máximo encontrado tão longe. Se for, então o seu programa deve atualizar o número máximo encontrado e conte o fato de você ter feito uma atualização. Exibir cada inteiro depois de você gerá-lo. Inclua uma notação com os inteiros que representam um novo máximo.

Depois de exibir 100 inteiros, seu programa deve exibir o máximo valor encontrado, junto com o número de vezes que o valor máximo foi atualizado durante o processo. A saída parcial do programa é mostrada abaixo, com… representando os inteiros restantes que seu programa exibirá. Execute o seu programa várias vezes. É o número de atualizações realizadas no valor máximo o que você esperava?
"""
