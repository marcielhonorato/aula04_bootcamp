# Exercício 1: Crie uma lista com os números de 1 a 10 e use um loop para imprimir cada número elevado ao quadrado.

    # lista_numero = []

    # for num in range(1,11):
    #     num_quadrado = num**2
    #     lista_numero.append(num_quadrado)
    # print(lista_numero)

# Exercício 2: Dada a lista ["Python", "Java", "C++", "JavaScript"], remova o item "C++" e adicione "Ruby".

    # lista = ["Python", "Java", "C++", "JavaScript"]
    # lista.remove("C++")
    # lista.append("Ruby")

    # print(lista)

# Exercício 3: Crie um dicionário para armazenar informações de um livro, incluindo título, autor e ano de publicação. Imprima cada informação.

    # from typing import Dict, Any 

    # livro: dict ={
    #     "Titulo":"Game of Thrones",
    #     "Autor":"Estagiario",
    #     "Ano": 2005
    # }

    # for chave, valor in livro.items():
    #     print(f"{chave}: {valor}")

# Exercício 4: Escreva um programa que conta o número de ocorrências de cada caractere em uma string usando um dicionário.

    # def contar_caracteres (s):
    #     contagem = {}
    #     for caracetere in s:
    #         contagem[caracetere] = contagem.get(caracetere, 0) + 1
    #     return contagem

    # print(contar_caracteres("Python, jornada de dados, hello world" ))

# Exercício 5: Dada a lista ["maçã", "banana", "cereja"] e o dicionário {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}, calcule o preço total da lista de compras.

    # lista_compra =  ["cereja", "banana", "maçã",]
    # precos = {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}
    # total_compra = sum([precos[item] for item in lista_compra])
    # print(total_compra)

# 6. Eliminação de Duplicatas
# Objetivo: Dada uma lista de emails, remover todos os duplicados.

emails = ["user@example.com", "admin@example.com", "user@example.com", "manager@example.com"]
emails_unicos = list(set(emails))

print(emails_unicos)

# 7. Filtragem de Dados
# Objetivo: Dada uma lista de idades, filtrar apenas aquelas que são maiores ou iguais a 18.

# 8. Ordenação Personalizada
# Objetivo: Dada uma lista de dicionários representando pessoas, ordená-las pelo nome.

# 9. Agregação de Dados
# Objetivo: Dado um conjunto de números, calcular a média.

# 10. Divisão de Dados em Grupos
# Objetivo: Dada uma lista de valores, dividir em duas listas: uma para valores pares e outra para ímpares.

# 11. Atualização de Dados
# Objetivo: Dada uma lista de dicionários representando produtos, atualizar o preço de um produto específico.

# 12. Fusão de Dicionários
# Objetivo: Dados dois dicionários, fundi-los em um único dicionário.

# 13. Filtragem de Dados em Dicionário
# Objetivo: Dado um dicionário de estoque de produtos, filtrar aqueles com quantidade maior que 0.

# 14. Extração de Chaves e Valores
# Objetivo: Dado um dicionário, criar listas separadas para suas chaves e valores.

# 15. Contagem de Frequência de Itens
# Objetivo: Dada uma string, contar a frequência de cada caractere usando um dicionário.