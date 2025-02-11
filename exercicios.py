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

from typing import Dict, Any 

livro: dict ={
    "Titulo":"Game of Thrones",
    "Autor":"Estagiario",
    "Ano": 2005
}

for chave, valor in livro.items():
    print(f"{chave}: {valor}")

# Exercício 4: Escreva um programa que conta o número de ocorrências de cada caractere em uma string usando um dicionário.

# Exercício 5: Dada a lista ["maçã", "banana", "cereja"] e o dicionário {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}, calcule o preço total da lista de compras.