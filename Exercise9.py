#Resolução do Exercício 9 proposto pelo Prof Paulo Salvatore

"""
Exercício 9
Nome: Checando Múltiplos
Objetivo: Receber dois números e exibir se um é múltiplo do outro ou não.
Dificuldade: Principiante
1 - Escreva um programa que receba dois números, {numero1} e {numero2}:
2 - Se o {numero1} for múltiplo do {numero2} exiba na tela: "O número {numero1} é múltiplo do número {numero2}.";
3 - Caso contrário, exiba na tela: "O número {numero1} não é múltiplo do número {numero2}.";
"""

numero1 = int(input("Digite um numero: ")) 
numero2 = int(input("Digite um numero: "))

if (numero1 % numero2) == 0:
    print("O numero {} é múltiplo do número {}.".format(numero1,numero2))
else:
    print("O numero {} nao é múltiplo do número {}.".format(numero1,numero2))
    
