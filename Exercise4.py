# Resolução - incrementada -  do Exercício 4 do prof Paulo Salvatore
# Nome: Data e Hora


#funcao retorna se o ano é bissexto
def ano_bissexto(ano_verificar):
    if (((ano_verificar % 100) != 0) and ((ano_verificar % 4) == 0) or ((ano_verificar % 400) == 0)):
        print("e bissexto")
        return True
    else:
        print("nao e bissexto")
        return False


from datetime import datetime

data_sistema = datetime.now()
# o metodo now do objeto datetime possui atributos com informações da data
print("{}/{}/{} - {}h{}'{}\"".format(data_sistema.day, data_sistema.month, data_sistema.year, data_sistema.hour, data_sistema.minute, data_sistema.second))
# outra forma de exibir essa mensagem:
print(f"{data_sistema.day}/{data_sistema.month}/{data_sistema.year} - {data_sistema.hour}h{data_sistema.minute}'{data_sistema.second}\"")

dia = -1
mes = -1
ano = -1

while (ano < 0):
    ano = int(input("Digite um ano = "))

while (mes < 1 or mes > 12):
    mes = int(input("Digite um mes = "))

if (mes != 2):
    if (mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12):
        while (dia < 1 or dia > 31):
            dia = int(input("Digite um dia = "))
    else:
        while (dia < 1 or dia > 30):
            dia = int(input("Digite um dia = "))
else:
    if (ano_bissexto(ano)):
        while (dia < 1 or dia > 29):
            dia = int(input("Digite um dia = "))
    else:
        while (dia < 1 or dia > 28):
            dia = int(input("Digite um dia = "))

data_usuario = datetime(ano, mes, dia) #os argumento da funcao correspondem a data e devem estar na ordem, note que nao enviar valores serao atribuidos 0 a eles

#data.weekday() retorna inteiro, segunda = 0 ate domingo = 6
dias_semana = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sabado", "Domingo"]
dia_da_semana = dias_semana[data_usuario.weekday()]

print(f"{data_usuario.day}/{data_usuario.month}/{data_usuario.year} - Dia da Semana: {dia_da_semana}")

print("Diferenca entre a data atual e a digitada = " + str((data_sistema-data_usuario).days) + " dias")
