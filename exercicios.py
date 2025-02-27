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

    # dicionario1 = {"a": 1, "b": 2}
    # dicionario2 = {"c": 3, "d": 4}
    # dicionario_fundido = {**dicionario1,**dicionario2}

    # print(dicionario_fundido)

# 13. Filtragem de Dados em Dicionário
# Objetivo: Dado um dicionário de estoque de produtos, filtrar aqueles com quantidade maior que 0.

    # estoque = {"Teclado": 10, "Mouse": 0, "Monitor": 3, "CPU": 0}
    # estoque_maior_que_zero = {produto: quantidade for produto, quantidade in estoque.items() if quantidade > 0}

    # print(estoque_maior_que_zero)

# 14. Extração de Chaves e Valores
# Objetivo: Dado um dicionário, criar listas separadas para suas chaves e valores.

    # dicionario = {"a": 1, "b": 2, "c": 3}
    # chaves = list(dicionario.keys())
    # valores = list(dicionario.values())

    # print(chaves)
    # print(valores)

# 15. Contagem de Frequência de Itens
# Objetivo: Dada uma string, contar a frequência de cada caractere usando um dicionário.

        # texto = "engenharia de dados"

        # contador_carecetere = {}

        # for caracatere in texto:
        #     if caracatere in contador_carecetere:
        #        contador_carecetere[caracatere] += 1
        #     else:
        #        contador_carecetere[caracatere] = 1
        # print(contador_carecetere)

    # estado = dict()
    # brasil = list()

    # for c in range(0,3):
    #     estado["uf"] = str(input("Unidade Federativa: "))
    #     estado["sigla"] = str(input("Sigla: "))
    #     brasil.append(estado.copy())
        
    # print()
    # for e in brasil:
    #     for v in e.values():
    #         print(v, end=' ')
    #     print()

# 16.Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até 20. Seu programa deverá ler um numero 
# pelo teclado(entre 0 a 20) e mostrá-lo por extenso.

    # numero_extenso = ('zero' ,'um' ,'dois' ,'três' ,'quatro' ,'cinco' ,'seis' ,'sete' ,'oito' ,'nove' ,'dez' ,'onze' ,'doze' ,'treze' ,'quatorze' ,'quinze' ,'dezesseis' ,'dezessete' ,'dezoito' ,'dezenove' ,'vinte')

    # while True:
    #     num_dig = int(input("Digite um número entre 0 e 20: "))
    #     if  0 <= num_dig <= 20:
    #         print(f"Você digitou o número: {numero_extenso[num_dig]}")
    #         break
    #     print("Tente Novamente.", end='')


# 17.Crie uma tupla preenchida com os 20 primeiro colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação.Depois mostre
#A) - Apenas os 5 primeiro colocados, 
#B) Os útilmos 4 colocadod da tabela 
#C) Uma lista com os times em ordem alfabética 
#D) Em que posição está um determinado time

    # brasileirao = ('Botafogo' ,'Palmeiras' ,'Flamengo' ,'Fortaleza' ,'Internacional' ,'São Paulo' ,'Corinthians' 
    #                ,'Bahia' ,'Cruzeiro','Vasco' ,'Vitória' ,'Atlético Mineiro' ,'Fluminense','Grêmio' ,'Juventude' 
    #                ,'Red Bull Bragantino' ,'Athletico Paranaense' ,'Criciúma' ,'Atlético Goianiense' ,'Cuiabá')
    # print("-=" * 60)
    # print(f"Lista de times do Brasileirão: {brasileirao}")
    # print("-=" * 60)
    # print(f"Os 5 primeiros são: {brasileirao[0:5]}")
    # print("-=" * 60)
    # print(f"Os 4 últimos são: {brasileirao[-4:]}")
    # print("-=" * 60)
    # print(f"Times em ordem alfabética: {sorted(brasileirao)}")
    # print("-=" * 60)
    # print(f"O Flamengo esta na {brasileirao.index("Flamengo") + 1}ª posição da tabela")

# 18 Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números gerados 
# e também indique o menor e o maior valor que estão na tupla

    # from random import randint

    # numeros = (randint(1, 10),randint(1, 10),randint(1, 10),randint(1, 10),randint(1, 10))

    # print(f'Os valores sorteados foram: ', end='')
    # for num in numeros:
    #     print(f'{num}', end=' ')
    # print(f"\nO maior valor sorteado foi {max(numeros)}")
    # print(f"O menor valor sorteado foi {min(numeros)}")

# 19 Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final mostre: 
#A)Quantas vezes apareceu o valor 9 
#B)Em que posição foi digitado o primeiro valor 3 
#C)Quais foram os numeros pares

numeros = (int(input("Digite um número: ")),int(input("Digite outro número: ")),int(input("Digite mais um número: ")),int(input("Digite o último um número: ")))

cont_par = 0

print(f"Você digitou os valores: {numeros}")
print(f"O valor 9 apareceu {numeros.count(9)} vezes")
if 3 in numeros:
    print(f"O valor 3 apareceu na {numeros.index(3) + 1}ª posição")
else: 
    print(f"O valor 3 não foi digitado")
print(f"O valores pares digitados foram: ", end='')
for n in numeros:
    if n % 2 == 0:
        print(n, end=' ')
