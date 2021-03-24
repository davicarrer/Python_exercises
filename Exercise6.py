#Resolução do Exercício 6 proposto pelo Prof Paulo Salvatore

"""
Exercício 6
Nome: Catapulta
Objetivo: Receber o número de baterias e duração da bateria e calcular a quantidade de pedras que a catapulta irá soltar.
Dificuldade: Principiante
1 - Uma catapulta lançou 300 pedras em 5 baterias de 15 minutos, cada.
2 - Quantas pedras ela lançaria em 8 baterias de 7 minutos, cada?
3 - Crie um programa que receba os valores base para que a aplicação funcione de forma que, se alterarmos o número de bateriais e a duração de cada bateria, o programa funcione sem precisar de mais modificações.
"""

# calculo: a máquina lança 4 pedras/min

num_baterias = int(input("Digite o numero de baterias: "))
duracao_bateria = int(input("Digite a duracao das baterias (min): "))
print(f"A catapulta ira soltar um total de {4*duracao_bateria*num_baterias} pedras")
