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

    # emails = ["user@example.com", "admin@example.com", "user@example.com", "manager@example.com"]
    # emails_unicos = list(set(emails))

    # print(emails_unicos)

# 7. Filtragem de Dados
# Objetivo: Dada uma lista de idades, filtrar apenas aquelas que são maiores ou iguais a 18.

    # idades = [22, 15, 30, 17, 18]
    # idades_validas = [idade for idade in idades if idade >= 18]

    # print(idades_validas)

# 8. Ordenação Personalizada
# Objetivo: Dada uma lista de dicionários representando pessoas, ordená-las pelo nome.

    # pessoas = [
    #     {"nome": "Alice", "idade": 30},
    #     {"nome": "Bob", "idade": 25},
    #     {"nome": "Carol", "idade": 20}
    # ]
    # pessoas.sort(key=lambda pessoa : pessoa["nome"])

    # print(pessoas)

# 9. Agregação de Dados
# Objetivo: Dado um conjunto de números, calcular a média.

    # numeros = [10, 20, 30, 40, 50]
    # media = sum(numeros) / len(numeros)

    # print(f"Média: {media}")

# 10. Divisão de Dados em Grupos
# Objetivo: Dada uma lista de valores, dividir em duas listas: uma para valores pares e outra para ímpares.

    # valores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # par = ([valor for valor in valores if valor % 2 == 0])
    # impar = ([valor for valor in valores if valor % 2 == 1])

    # print(f"Valores Par: {par}")
    # print(f"Valores Impar: {impar}")

# 11. Atualização de Dados
# Objetivo: Dada uma lista de dicionários representando produtos, atualizar o preço de um produto específico.

    # produtos = [
    #     {"id": 1, "nome": "Teclado", "preço": 100},
    #     {"id": 2, "nome": "Mouse", "preço": 80},
    #     {"id": 3, "nome": "Monitor", "preço": 300}
    # ]

    # # Atualizar o preço do produto com id 2 para 90

    # for produto in produtos:
    #     if produto["id"] == 2:
    #        produto["preço"] = 90
    # print(produtos)

# 12. Fusão de Dicionários
# Objetivo: Dados dois dicionários, fundi-los em um único dicionário.

dicionario1 = {"a": 1, "b": 2}
dicionario2 = {"c": 3, "d": 4}
dicionario_fundido = {**dicionario1,**dicionario2}

print(dicionario_fundido)


# 13. Filtragem de Dados em Dicionário
# Objetivo: Dado um dicionário de estoque de produtos, filtrar aqueles com quantidade maior que 0.

# 14. Extração de Chaves e Valores
# Objetivo: Dado um dicionário, criar listas separadas para suas chaves e valores.

# 15. Contagem de Frequência de Itens
# Objetivo: Dada uma string, contar a frequência de cada caractere usando um dicionário.