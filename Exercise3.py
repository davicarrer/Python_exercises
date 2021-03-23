#Resolução baseada no Exercício 3 disponibilizado pelo prof Paulo Salvatore

nome = input("Digite seu nome = ").capitalize()
idade = -1
while (idade < 0):
    idade = float(input("Digite sua idade = "))
    if (idade < 0):
        print("Impossivel ter essa idade")

genero = input("Digite o genero com o qual voce se identifica = ")

mensagem = "Ola, " + nome + ", voce possui " + str(idade)
if (idade == 0 or idade == 1):
    mensagem = mensagem + " ano "
else:
    mensagem = mensagem + " anos "
mensagem = mensagem + "de idade e e do genero " + genero + ". Ja pensou no que vc fara no seu aniversario de " + str(idade+1)
if (idade == 0):
    mensagem = mensagem + " ano?"
else:
    mensagem = mensagem + " anos?"

print(mensagem)