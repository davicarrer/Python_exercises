#Resolução do Exercício 12 proposto pelo Prof Paulo Salvatore

#1 - Sendo f(x) = 3x - 2 determine o valor de f(5) + f(0).

def funcao1(x):
    return(3*x-2)

print("f(5) + f(0) = {}".format(funcao1(5)+funcao1(0)))

#2 - Na produção de peças, uma fábrica tem um custo fixo de R$ 30,00 mais um custo variável de R$ 2,00 por unidade produzida. Sendo x o número de peças unitárias produzidas, determine o custo de produção de 100 peças.

def funcao2(x):
    return (30+2*x)

print("O custo de produção de 100 peças é R$",funcao2(100))

#3 - Crie uma função que receba 2 números e retorne o maior valor.

def funcao3(x,y):
    if (x>=y):
        return(x)
    else:
        return(y)

#4 - Crie uma função que receba 3 números e retorne o maior valor, use a função da questão 3.

def funcao4(x,y,z):
    return (funcao3(funcao3(x,y),funcao3(y,z)))

num1 = int(input("Digite 3 numeros! 1º: "))
num2 = int(input("2º: "))
num3 = int(input("3º: "))
print("O maior é: ",funcao4(num1,num2,num3))

#5 - Dadas as funções f(x) = x – 5 e g(x) = 3x + 1, crie um código que retorne o valor da soma de f(9) + g(2). Depois crie um código que retorne o valor da soma das duas funções com números digitados pelo usuário.

def funcao5f(x):
    return(x-5)

def funcao5g(x):
    return(3*x-1)

print("f(9) + g(2) = ", (funcao5f(9)+funcao5g(2)))
num1 = int(input("Digite um numero: "))
num2 = int(input("Digite outro numero: "))
print(f"f({num1}) + g({num2}) = {(funcao5f(num1)+funcao5g(num2))}")

#6 - Considere as seguintes funções: f(x) = x - 4 e g(x) = 5x + 1. Qual é o valor da função composta g(f(3))? Depois crie um código que retorne o valor da soma das duas funções com números digitados pelo usuário.

def funcao6f(x):
    return(x-4)

def funcao6g(x):
    return(5*x+1)

print("O valor da função composta g(f(3)) = ",funcao6g(funcao6f(3)))


#7 - Crie uma função chamada dado() que retorna, através de sorteio, um número de 1 até 6. Exiba 10 números sorteados utilizando a mesma função criada.

import random 
def dado():
    return(random.randint(1,6))

print(dado(),dado(),dado(),dado(),dado(),dado(),dado(),dado(),dado(),dado())

