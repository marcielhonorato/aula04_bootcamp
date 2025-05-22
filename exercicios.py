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

    # numeros = (int(input("Digite um número: ")),int(input("Digite outro número: ")),int(input("Digite mais um número: ")),int(input("Digite o último um número: ")))

    # cont_par = 0

    # print(f"Você digitou os valores: {numeros}")
    # print(f"O valor 9 apareceu {numeros.count(9)} vezes")
    # if 3 in numeros:
    #     print(f"O valor 3 apareceu na {numeros.index(3) + 1}ª posição")
    # else: 
    #     print(f"O valor 3 não foi digitado")
    # print(f"O valores pares digitados foram: ", end='')
    # for n in numeros:
    #     if n % 2 == 0:
    #         print(n, end=' ')

# 20 Crie um programa que tenha uma tupla única com nomes de produtos e seus respctivos preços, na sequência. No final, 
# mostre uma listagem de preços, organizando os dados em uma forma tabular

    # produtos = ("Pc Desktop", 1900, 
    #             "Mouse RTX", 445.90, 
    #             "Teclado Mecânico", 699, 
    #             "Impressora Epson", 1300,
    #             "Headset GT500", 329.99, 
    #             "Placa de Video GTX 4060", 3200,
    #             "Modem TP LINK" , 255,
    #             "Fone de Ouvido" , 79.90,
    #             "Placa Mães AM5" , 799, 
    #             "Computador Ryzen 7 7700x", 8000
    #             )

    # print('-=' * 30)
    # print(f'{"LISTAGEM DE PRODUTOS E PREÇOS":^60}')
    # print('-=' * 30)

    # for pos in range(0, len(produtos)):
    #     if pos % 2 == 0:
    #         print(f'{produtos[pos]:.<40}', end='')
    #     else:
    #         print(f'R${produtos[pos]:>10.2f}')
    # print('--' * 30)

# 21 Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quasi são suas vogais

# palavras = ('hoje', 'casa', 'python', 'progarama', 'computador', 'processador')

# for palavra in palavras:
#     print(f'\nNa palavra {palavra.upper()} temos ', end='')
#     for letra in palavra:
#         if letra.lower() in 'aeiou':
#             print(letra, end=' ')

# 22 Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, 
# mostre qual foi o maior e o menor valor digitado e as suas repectivas posições na lista

# valores = []

# for cont in range(0, 5):
#     valores.append(int(input(f'Digite um valor para a posição {cont} : ')))

# print('-=' * 30)    
# print(f'Você digitou os valores {valores}')

# print(f'O maior valor digitado foi {max(valores)}, nas posições ', end='')
# for pos, num in enumerate(valores):
#     if  num == max(valores):
#         print(f'{pos}...', end='')   

# print(f'\nO menor valor digitado foi {min(valores)}, nas posições ', end='')
# for pos, num in enumerate(valores):
#     if  num == min(valores):
#         print(f'{pos}...', end='')  

# 23 Crie um programa que o usuario possa digitar vários valores númericos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado.
# no final, serão exibidos todos os valores únicos digitado em ordem crescente.

# lista_numero = []

# while True:
#     numero = int(input("Digite um valor númerico: "))
#     if numero not in lista_numero:
#         lista_numero.append(numero)
#         print("Valor adicionado com sucesso...")
#     else:
#         print("Valor duplicado! Não será possivel adicioná-lo")
#     continuar = str(input("Deseja continuar (S/N): "))
#     if continuar in 'Nn':
#        break
# lista_numero.sort()
# print("-=" * 40)
# print(f"Você digitou os valores {lista_numero}")

# 24 Crie um programa onde o usuário possa digitar cinco valores númericos e cadastre-os em uma lista. Já na posição correta de inserção (sem usar o sort()), 
# No final, mostre a lista ordenada na tela.

# lista_valores = []

# for c in range(0, 5):
#     valor = int(input("Digite um valor numérico: "))
#     if c == 0 or valor > lista_valores[-1]:
#         lista_valores.append(valor)
#         print('Adicionado ao final da lista...')
#     else:
#         pos = 0
#         while pos < len(lista_valores):
#             if valor <= lista_valores[pos]:
#                 lista_valores.insert(pos,valor)
#                 print(f'Adicionado na posição {pos} da lista')
#                 break
#             pos += 1
        
# print('-=' * 30)        
# print(lista_valores)

# 25 Crie um programa que vai ler vários números e colocar em uma lista. Depois disso: 
# A)Quantos números foram digitados. 
# B) A lista de valores, ordenada de forma descrescente. 
# C)Se o valor 5 foi digitado e está ou não na lista.

# lista_numeros = []

# while True:
#     num = int(input('Digite um valor: '))
#     lista_numeros.append(num)
#     continuar = str(input('Deseja continuar (S/N): ')).upper()
#     if continuar == 'N':
#         break


# print('-=' * 30)    
# print(f'Você digitou {len(lista_numeros)} elementos')
# print(f'O valores em ordem descrescente são {lista_numeros[::-1]}')
# if 5 in lista_numeros:
#         print('O valor 5 faz parte da lista')
# else:
#     print('O valor 5 não faz parte da lista!')

# 26 Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os 
# valores pares e os valores ímpares digitados, respctivamente. Ao final mostre o contepudo das três listas geradas.

# numeros_lista = []

# while True:
#     numero = int(input('Digite um número: '))
#     numeros_lista.append(numero)
#     continuar = str(input('Deseja continuar (S/N)? '))
#     if continuar in 'Nn':
#         break
# print(f'A lista complea é {numeros_lista}')
# print(f'A lista de pares é {[x for x in numeros_lista if x % 2 == 0]}')
# print(f'A lista de impares é {[x for x in numeros_lista if x % 2 == 1]}')

# 27 Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão passada 
# esta com os parênteses abertos e fechados na ordem coreta.

# expressao = str(input('Digite a expressão: '))
# pilha_parenteses = []

# for simb in expressao:
#     if simb == '(':
#         pilha_parenteses.append('(')
#     elif simb == ')':
#         if len(pilha_parenteses) > 0:
#             pilha_parenteses.pop()
#         else:
#             pilha_parenteses.append(')')
#             break
# if len(pilha_parenteses) == 0:
#     print('Sua expressão esta correta!')
# else:
#     print('Sua expressão esta errada!')

# 28 Faça um programa que leia nome e peso de várias pessoa, guardando tudo em uma lista. No final mostre 
# A) Quantas pessoas foram cadastradas 
# B) Uma listagem com as pessoas mais pesadas 
# C) Uma listagem com as pessoas mais leves


# cadastro_pessoas = list()

# dados_pessoa = list()

# lista_peso_pessoa = list()

# lista_maior_peso = list()

# lista_menor_peso = list()

# while True:
#     nome = str(input('Digite o nome: '))
#     dados_pessoa.append(nome)
#     peso = int(input('Digite o peso: '))
#     dados_pessoa.append(peso)
#     cadastro_pessoas.append(dados_pessoa[:])   
#     dados_pessoa.clear()
#     continuar = str(input('Deseja continuar N/S: ' ))
#     if continuar in ('Nn'):
#         break;

# for pessoa in cadastro_pessoas:
#     lista_peso_pessoa.append(pessoa[1])

# for pessoa_peso in cadastro_pessoas:
#     if pessoa_peso[1] == max(lista_peso_pessoa):
#         lista_maior_peso.append(pessoa_peso[0])
#     elif pessoa_peso[1] == min(lista_peso_pessoa):
#         lista_menor_peso.append(pessoa_peso[0])
        
# print('-=' * 30)

# print(f'Ao todo, você cadastrou {len(cadastro_pessoas)} pessoas')
# print(f'O maior peso foi {max(lista_peso_pessoa)}. Peso de {lista_maior_peso}.')
# print(f'O menor peso foi {min(lista_peso_pessoa)}. Peso de {lista_menor_peso}.')


# cadastro_pessoas = list()

# dado_temp = list()

# peso_min = peso_max = 0

# while True:
#     dado_temp.append(str(input('Digite o nome: ')))
#     dado_temp.append(int(input('Digite o peso: ')))
    
#     if len(cadastro_pessoas) == 0:
#         peso_min = peso_max = dado_temp[1]
#     else:
#         if dado_temp[1] > peso_max:
#             peso_max = dado_temp[1]
#         if dado_temp[1] < peso_min:
#             peso_min = dado_temp[1]
#     cadastro_pessoas.append(dado_temp[:])
#     dado_temp.clear()
#     continuar = str(input('Deseja continuar (N/n): '))
#     if continuar in 'Nn':
#         break

# print('-=' * 30)
# print(f'Ao todo, você cadastrou {len(cadastro_pessoas)} pessoas.')

# print(f'O maior peso foi {peso_max}. Peso de ', end='')
# for pessoa in cadastro_pessoas:
#     if peso_max == pessoa[1]:
#         print(f'[{pessoa[0]}] ', end='')

# print()
# print(f'O menor peso foi {peso_min}. Peso de ', end='')
# for pessoa in cadastro_pessoas:       
#     if peso_min == pessoa[1]:
#        print(f'[{pessoa[0]}] ', end='')

# 29 Criar um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista unica que mantenha separados os valores pares e ímpares. 
# No final, mostre os valores pares e impares em ordem crescente.

# lista_pares_impares =[[], []]

# for pos in range(1,8):
#     numero = int(input(f'Digite o {pos}º numero: '))
#     if numero % 2 == 0:
#         lista_pares_impares[0].append(numero)
#     else:
#         lista_pares_impares[1].append(numero)

# print('-=' * 30)

# lista_pares_impares[0].sort()
# lista_pares_impares[1].sort()
# print(f'Os valores pares digitados foram: {lista_pares_impares[0]}')
# print(f'Os valores impares digitados foram: {lista_pares_impares[1]}')

# 30 Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.No final, mostre a matriz na tela, com a formatação correta

# matriz = [[0,0,0], [0,0,0], [0,0,0]]

# for i in range(0,3):
#     for j in range(0,3):
#         matriz[i][j] = int(input(f'Digite um valor para [{i},{j}]: '))

# print('-=' * 30)

# for i in range(0,3):
#     print(end='')
#     for j in range(0,3):
#         print(f'[{matriz[i][j]:^5}]', end='')
#     print()

# 31 Aprimore o desafio anterior, mostrando no final: 
# A) A soma de todas os valores pares digitados. 
# B) A somados valores da terceira coluna.
# C) O maior valor da segunda linha.

# matriz = [[0,0,0], [0,0,0], [0,0,0]]

# soma_pares = soma_terceira_coluna = maior_valor = 0

# for i in range(0,3):
#     for j in range(0,3):
#         matriz[i][j] = int(input(f'Digite um valor para [{i},{j}]: '))

# print('-=' * 30)

# for h in range(0,3):
#     for f in range(0,3):
#         if matriz[h][f] % 2 == 0:
#             soma_pares += matriz[h][f]
#         print(f'[{matriz[h][f]:^5}]', end='')
#     print()

# print('-=' * 30)

# for pos_soma in range(0, 3):
#     soma_terceira_coluna += matriz[pos_soma][2]

# for pos_max in range(0, 3):
#     if  matriz[1][pos_max] > maior_valor:
#         maior_valor = matriz[1][pos_max]

# print(f'A soma dos valores pares é {soma_pares}.')
# print(f'A soma dos valores da terceira coluna é {soma_terceira_coluna}.')
# print(f'O maior valor da segunda linha é {maior_valor}.')

# 32 Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar quantos jogos serão gerados e 
# vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

# from random import randint
# from time import sleep

# print("-" * 30)
# print('        JOGA NA MEGA SENA        ')
# print("-" * 30)

# quantidade_jogos = int(input(("Quantos jogos você quer que eu sorteie? ")))

# lista_jogos = list()
# lista_numeros = list()

# contador_numeros_jogos = 1

# while contador_numeros_jogos <= quantidade_jogos:
#     contador_numeros = 0
#     while True:
#         numero = randint(1, 60) 
#         if numero is not lista_numeros:
#             lista_numeros.append(numero)
#         contador_numeros += 1
#         if contador_numeros >= 6:
#             break
#     lista_numeros.sort()
#     lista_jogos.append(lista_numeros[:])
#     lista_numeros.clear()
#     contador_numeros_jogos += 1

# print()
# print('-=' * 3, f'SORTEANDO {quantidade_jogos} JOGOS','-=' * 3)
# print()

# for pos, i in enumerate(lista_jogos):
#     print(f'Jogo {pos + 1} : {i}')
#     sleep(1)

# print()
# print('-=' * 5, '< BOA SORTE! >','-=' * 5)

# 33 Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um 
# e permitindo que o usuário possa mostrar as notas de cada aluno individualmente.

# ficha = list()

# while True:
#     nome = str(input('Nome: '))
#     nota1 = float(input('Nota 1: '))
#     nota2 = float(input('Nota 2: '))
#     media = (nota1 + nota2) / 2
#     ficha.append([nome,[nota1, nota2], media])
#     resposta = str(input('Cadastrar mais alunos (S/N): '))
#     if resposta in 'Nn':
#         break
# print('-=' * 30)
# print(f'{"Nº":<4} {"Nome":<10} {"Media":>8}')

# for pos, aluno in enumerate(ficha):
#     print(f'{pos:<4} {aluno[0]:<10} {aluno[2]:>8.1f}')

# while True:
#     print('-' * 35)
#     mostrar_nota_aluno = int(input('Mostrar nota de qual aluno (999 para sair): '))
#     if mostrar_nota_aluno == 999:
#         print( 'FINALIZANDO...')
#         break
#     if mostrar_nota_aluno <= len(ficha) - 1:
#         print(f'Notas de {ficha[mostrar_nota_aluno][0]} são [{ficha[mostrar_nota_aluno][1]}]')
# print('<<< VOLTE SEMPRE >>>')

# 34 Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.

# aluno = dict()

# aluno['nome'] = str(input('Nome: '))
# aluno['media'] = float(input(f'Média de {aluno['nome']} : '))
# if aluno['media'] >= 7.0:
#     aluno['situacao'] = 'Aprovado'
# elif  5 <= aluno['media'] < 7:
#      aluno['situacao'] = 'Recuperação'
# else:
#     aluno['situacao'] = 'Reprovado'
# print('-=' * 30)
# for chave, valor in aluno.items():
#     print(f' - {chave} é igual a {valor}')

# 35 Crie um programa onde 4 jogadres joguem um dado e tenham resultados em um dicionário. No final, coloque esse dicionário em ordem, 
# sabendo que o vencedor tirou o maior número no dado.

# from random import randint
# from operator import itemgetter
# from time import sleep

# jogo_dado = {'jogador1': randint(1,6), 
#              'jogador2': randint(1,6), 
#              'jogador3': randint(1,6), 
#              'jogador4': randint(1,6)}

# ranking = list()

# print('Valores Sorteados:')

# for jogador, valor_dado in jogo_dado.items():
#     print(f'{jogador} tirou {valor_dado} no dado.')
#     sleep(1)
# ranking = sorted(jogo_dado.items(), key=itemgetter(1), reverse=True)

# print('-=' * 30)
# print('  == RANKING DOS JOGADORES ==')

# for pos, rank in enumerate(ranking):
#     print(f'  {pos + 1}º lugar: {rank[0]} com {rank[1]}')
#     sleep(1)

# 34 Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário 
# se por acaso o CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. 
# Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar (35 anos de contribuição).

# from datetime import datetime as dt

# cadastro_pessoa = dict()

# cadastro_pessoa['Nome'] = str(input('Nome: '))
# ano_nascimento = int(input('Ano de Nascimento: '))
# cadastro_pessoa['Idade'] = dt.today().year - ano_nascimento
# cadastro_pessoa['Nº CTPS'] = int(input('Carteira de Trabalho (0 não tem): '))

# if cadastro_pessoa['Nº CTPS'] != 0:
#     cadastro_pessoa['Ano de Contratação'] = int(input('Ano de Contratação: '))
#     cadastro_pessoa['Salário'] = float(input('Salário R$: '))
#     cadastro_pessoa['Aposentadoria'] =  (cadastro_pessoa['Ano de Contratação'] - ano_nascimento) + 35  #cadastro_pessoa['Idade'] + (cadastro_pessoa['Ano de Contratação'] + 35) - dt.now().year
#     print(cadastro_pessoa)
# else:
#     print(cadastro_pessoa)
# print('-=' * 30)
# for chave, valor in cadastro_pessoa.items():
#     print(f'- {chave} tem o valor {valor}')

# 35 Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler 
# a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário,incluindo o total de gols feitos durante o campeonato

# jogador = dict()
# partidas_gols = list()
# jogador['nome'] = str(input('Nome do Jogador: '))
# total_partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou?: '))
# for cont in range(0, total_partidas):
#     partidas_gols.append(int(input(f'    Quantos gols na partida {cont+1}: ')))
# jogador['gols'] = partidas_gols[:]
# jogador['total'] = sum(partidas_gols)
# print('-=' * 30)
# print(jogador)
# print('-=' * 30)
# for chave, valor in jogador.items():
#     print(f'O campo {chave} tem o valor {valor}.')
# print('-=' * 30)
# print(f'O jogador {jogador["nome"]}, jogou {total_partidas} partidas.')
# for i, gol in enumerate(jogador['gols']):
#     print(f'     => Na partida {i + 1}, fez {gol} gols.')
# print(f'Foi um total de {jogador["total"]} gols.')

# 36 Crie um programa que leia nome, sexo e idade de várias pessoas, gurdando os dados de cada pessoa em um dicionário e todos o dicionário em uma lista, 
# no final mostrar:
# A) Quantas pessoas foram cadastradas. 
# B) A média de idade do grupo. 
# C) Uma lista com todas as mulheres. 
# D) Uma lista com todas a pessoas com idade acima da média

# grupo_pessoa = list()
# pessoa = dict()
# soma = 0
# while True:
#     pessoa['nome'] = str(input('Nome: '))
#     while True:
#         pessoa['sexo'] = str(input('Sexo: ')).upper()
#         if pessoa['sexo'] in 'MF':
#             break
#         print('ERRO! Por favor digite apenas M ou F.')
#     pessoa['idade'] = int(input('Idade: ')) 
#     soma += pessoa['idade']
#     grupo_pessoa.append(pessoa.copy())  
#     while True:
#         resposta = str(input('Deseja cadastrar mais pessoas (S/N):')).upper()
#         if resposta in 'SN':
#             break
#         print('Responda apenas S ou N')  
#     if resposta == 'N':
#         break   
# print('-=' * 30)
# media = soma / len(grupo_pessoa)
# print(f'A) Ao todo de {len(grupo_pessoa)} pessoas cadastradas.')
# print(f'B) A média de idade é de {media:.2f} anos.')
# print('As mulheres cadastradas foram ', end='')
# for p in grupo_pessoa:
#     if p['sexo'] == 'F':
#         print(f'{p['nome']} ', end='')
# print()
# print(f'D) Uma lista com todas a pessoas com idade acima da média: ', end='')
# for p in grupo_pessoa:
#     if p['idade'] >= media:
#         print('     ', end='')
#         for k, v in p.items():
#             print(f'{k}={v} ', end='')
# print('<< ENCERRADO >>')


# 37) Aprimore o DESAFIO 35 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.

time = list()
jogador = dict()
partidas = list()
while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do Jogador: '))
    total = int(input(f'Quantas partidas {jogador['nome']}: '))
    for c in range(0,total):
        partidas.append(int(input(f'    Quantos gols na partida {c+1}: ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    partidas.clear()
    while True:
        resposta = str(input('Deseja continuar (S/N) ?:')).upper()
        if resposta in 'SN':
            break
        print('ERRO!. Responda paenas S ou N')
    if resposta == 'N':
        break
print('-=' * 30)
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<20}', end='')
print()
print('--' * 30)
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<20}', end='')
    print()
print('--' * 30)
while True:
    busca = int(input('Mostrar dados de qual jogador (999 para parar): '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'Erro!. Não existe o jogador com o código {busca}!')
    else:
        print(f' -- LEVATAMENTO DO JOGADOR {time[busca]['nome']} ')
        for i, g in enumerate(time[busca]['gols']):
            print(f'    No jogo {i+1} fez {g} gol(s)')
print('<< VOLTE SEMPRE >>')
    
