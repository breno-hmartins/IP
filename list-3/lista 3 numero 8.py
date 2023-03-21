soma = 0
media = 0
n = int(input("Quantos números deseja inserir ara calcular a média ?\n"))
for i in range(0,n):
    x = int(input("informe os valores.\n"))
    soma += x
    media = soma / n
print("A média é igual a", media)