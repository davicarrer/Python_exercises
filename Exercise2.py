# Resolução baseada no exercício 2 disponibilizado pelo prof Paulo Salvatore

total_conta = float(input("Digite o total da conta = "))
valor_pago = total_conta -1 
while (valor_pago < total_conta):
    valor_pago = float(input("Digite o valor pago = "))
    if (valor_pago < total_conta):
        print("O valor pago deve ser maior ou igual que o valor da conta!")

troco = valor_pago - total_conta
print("O troco é = ", troco)
print(f"O troco é = R${troco:.2f}")
print (f"O total da conta foi de R${total_conta:.2f}, você pagou R${valor_pago:.2f} e o seu troco foi de R${troco:.2f}.")
