#Resolução do Exercício 8 proposto pelo Prof Paulo Salvatore

"""
Exercício 8
Nome: Comparação de Números: Maior, Menor ou Igual
Objetivo: Receber dois números e exibir qual é maior, menor ou igual a quem.
Dificuldade: Principiante
1 - Escreva um programa que receba dois números, {numero1} e {numero2}:
2 - Caso o {numero1} seja maior do que o {numero2}, exiba na tela: "O número {numero1} é maior do que o número {numero2}.";
3 - Caso contrário, se o {numero1} for menor, exiba: "O número {numero1} é menor que {numero2}.";
4 - Caso contrário, exiba: "O número {numero1} é igual ao número {numero2}.".
"""

numero1 = float(input("Digite um número qualquer: "))
numero2 = float(input("Digite outro número qualquer: "))
mensagem = "O número " + str(numero1) + " é "
if (numero1 >= numero2):
    if(numero1 > numero2):
        mensagem = mensagem + "maior do que o"
    else:
        mensagem = mensagem + "igual ao"
else:
    mensagem = mensagem + "menor do que o"
mensagem = mensagem + " número " + str(numero2)
print(mensagem)