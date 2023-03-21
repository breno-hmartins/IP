soma = 0
for i in range (0,20):
    x = int(input("Informe o valor: "))
    if x **2 > 255:
        continue
    else:
        soma += x
print("A soma de todos os números cujo o quadrado seja menor que 255 é igual a", soma)
