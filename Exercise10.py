#Resolução do Exercício 10 proposto pelo Prof Paulo Salvatore

"""
Exercício 10
Nome: A de Amor, B de Baixinho
Objetivo: Receber o nome, extrair a primeira letra e fazer comparações.
Dificuldade: Principiante
1 - Escreva um programa que receba o nome de uma pessoa;
2 - Extraia a primeira letra do nome;
3 - Compare a primeira letra de modo que, caso seja "A", exiba na tela "A de Amor", caso seja "B", exiba na tela "B de Baixinho", caso contrário, exiba na tela "Seu nome não é legal.";
4 - Faça com que o programa funcione indepente se for digitado um nome com letras minúsculas ou maiúsculas.
"""

nome = input("Digite um nome: ").upper()
if (nome[0] == "A"):
    print("A de Amor")
elif (nome[0] == "B"):
    print("B de Baixinho")
else:
    print("Seu nome não é legal.")
